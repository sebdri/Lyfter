def requires_login(func):
    def wrapper(*args, **kwargs):
        if user_logged_in != True:
            raise ValueError("User not authenticated")
        return func(*args, **kwargs)
    return wrapper


@requires_login
def profile():
    print("Data of the secret profile")



user_logged_in = True

try:
    profile()
    print("❌ Fail")
except ValueError as e:
    print(f"✅ OK -> {e}")

# Caso 2: usuario SÍ logueado -> debería ejecutar la función
user_logged_in = True
resultado = profile()
print(f"✅ OK: {resultado}" if resultado == "Datos del perfil secreto" else "❌ Fail")


