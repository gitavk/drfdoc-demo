import ast
from rest_framework import serializers

from scenario.models import Scenario, Task
from .task import TaskSerializer


class ScenarioSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Scenario
        fields = '__all__'

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
        self.add_tasks(instance, data)
        return instance
