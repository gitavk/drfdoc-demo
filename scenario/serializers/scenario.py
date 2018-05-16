import ast
from rest_framework import serializers

from scenario.models import Scenario, Task
from .task import TaskSerializer


class ScenarioSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Scenario
        fields = '__all__'

    def get_tasks(self, obj):
        qs = obj.tasks.extra(
            select={'creation_seq': 'scenario_scenario_tasks.id'}
            ).order_by("creation_seq")
        return TaskSerializer(qs, many=True).data

    def get_or_create_task(self, data):
        qs = Task.objects.filter(pk=data.get('id'))
        if qs.exists():
            return qs.first()
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        return task

    def add_tasks(self, instance, data):
        tasks = data.get('tasks', [])
        # added to test from drf doc
        if isinstance(tasks, type('')):
            tasks = ast.literal_eval(tasks)
        for task_data in tasks:
            task = self.get_or_create_task(task_data)
            instance.tasks.add(task)

    def create(self, validated_data):
        instance = super().create(validated_data)
        data = self.context.get('request').data
        self.add_tasks(instance, data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        data = self.context.get('request').data
        # clean exists tasks to save sequence as in update
        instance.tasks.all().delete()
        self.add_tasks(instance, data)
        return instance
