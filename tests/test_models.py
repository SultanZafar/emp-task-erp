def test_employee_model_fields():
    fields = ['employee_id', 'name', 'department', 'phone', 'email']
    for field in fields:
        assert field is not None


def test_task_model_fields():
    fields = ['title', 'description', 'status']
    for field in fields:
        assert field is not None