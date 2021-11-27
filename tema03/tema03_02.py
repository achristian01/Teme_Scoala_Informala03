import json
import copy
import csv
import uuid

# Presupunand ca as fi rezolvat concatenarea

[{'id': UUID('293dadb2-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Hyundai', 'Model': 'Santa_Fe', 'hp': 189, 'price': 30000, 'slow car': False, 'fast car': False, 'sport car': True},
{'id': UUID('293dadb3-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Kia', 'Model': 'Sorento', 'hp': 140, 'price': 20000, 'slow car': False, 'fast car': True, 'sport car': False},
{'id': UUID('293dadb4-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'BMW', 'Model': 'X6', 'hp': 5233, 'price': 110000, 'slow car': False, 'fast car': False, 'sport car': True},
{'id': UUID('293dadb5-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Mercedes', 'Model': "'Gelandewagen'", 'hp': 416, 'price': 120000, 'slow car': False, 'fast car': False, 'sport car': True},
{'id': UUID('293dadb6-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Dacia', 'Model': 'Logan', 'hp': 87, 'price': 10000, 'slow car': True, 'fast car': False, 'sport car': False},
{'id': UUID('293dadb7-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'VW', 'Model': 'Golf-1', 'hp': 75, 'price': 800, 'slow car': True, 'fast car': False, 'sport car': False},
{'id': UUID('293dadb8-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Opel', 'Model': 'Vectra', 'hp': 130, 'price': 4800, 'slow car': False, 'fast car': True, 'sport car': False}



[{'id': UUID('293dadb2-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Hyundai', 'Model': 'Santa_Fe', 'hp': 189, 'price': 30000, 'cheap': False, 'medium': False, 'sport': True},
{'id': UUID('293dadb3-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Kia', 'Model': 'Sorento', 'hp': 140, 'price': 20000, 'cheap': False, 'medium': False, 'sport': True},
{'id': UUID('293dadb4-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'BMW', 'Model': 'X6', 'hp': 5233, 'price': 110000, 'cheap': False, 'medium': False, 'sport': True},
{'id': UUID('293dadb5-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Mercedes', 'Model': "'Gelandewagen'", 'hp': 416, 'price': 120000, 'cheap': False, 'medium': False, 'sport': True},
{'id': UUID('293dadb6-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Dacia', 'Model': 'Logan', 'hp': 87, 'price': 10000, 'cheap': False, 'medium': False, 'sport': True},
{'id': UUID('293dadb7-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'VW', 'Model': 'Golf-1', 'hp': 75, 'price': 800, 'cheap': True, 'medium': False, 'sport': False},
{'id': UUID('293dadb8-4f47-11ec-800b-e74e315f0f2e'), 'Brand': 'Opel', 'Model': 'Vectra', 'hp': 130, 'price': 4800, 'cheap': False, 'medium':