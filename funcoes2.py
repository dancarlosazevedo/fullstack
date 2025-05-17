def login_usuario(perfil):
    print(f"{'bem  vindo admin' if perfil.lower() == 'admin' else 'bem vindo usuario'}") 
    
login_usuario('Admin')
login_usuario('admin')
login_usuario('User')
login_usuario('usuário')