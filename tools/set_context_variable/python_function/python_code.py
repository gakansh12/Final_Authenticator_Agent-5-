def set_context_variable(req: dict) -> dict:
    return {'ok': True, 'key': req.get('key'), 'value': req.get('value')}
