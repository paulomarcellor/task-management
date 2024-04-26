from django import forms
from tasks.models import dataTask, stepsTask

import requests

class taskForm(forms.ModelForm):
    class Meta:
        model = dataTask
        fields = ['name', 'category', 'start', 'deadline', 'status', 'aap']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__newtask__input', 'required': True}),
            'category': forms.TextInput(attrs={'class': 'form__newtask__input', 'required': True}),
            'start': forms.DateInput(attrs={'class': 'form__newtask__input', 'type':'date', 'required': True}),
            'deadline': forms.DateInput(attrs={'class': 'form__newtask__input', 'type':'date', 'required': True}),
            'status': forms.Select(attrs={'class': 'form__newtask__select', 'required': True}),
            'aap': forms.CheckboxInput(attrs={'class': 'form__newtask__input'})
        }

class stepsTaskForm(forms.ModelForm):
    class Meta:
        model = stepsTask
        fields = ['task', 'step', 'step_start', 'step_end', 'done']
    
    def save_and_post_to_api(self):
        # Salva os dados do formulário no banco de dados local
        new_steps_task = super().save()

        # Prepara os dados para enviar para a API
        data = {
            'task': new_steps_task.task.id,
            'step': new_steps_task.step,
            'step_start': new_steps_task.step_start,
            'step_end': new_steps_task.step_end,
            'done': new_steps_task.done
        }

        # Envia uma requisição POST para a API para criar um novo registro
        api_url = "http://localhost:8000/api/steps/"
        response = requests.post(api_url, data=data)

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 201:
            print("Novo registro criado na API com sucesso!")
        else:
            print("Erro ao criar novo registro na API:", response.text)