# pip install pyesapi
import pyesapi
def main():
    try:
        app = pyesapi.CustomScriptExecutable.CreateApplication('python_ex')  # script name is used for logging
        print("Current User: " + app.CurrentUser.ToString())
        print([p.Id for p in app.PatientSummaries])

    finally:
        app.Dispose()

if __name__ == "__main__":
    main()
