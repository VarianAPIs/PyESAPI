import pysapi  # pip install git+https://github.com/VarianAPIs/PyESAPI

def main():
    try:
        app = pysapi.CustomScriptExecutable.CreateApplication('python_ex')  # script name is used for logging
        print("Current User: " + app.CurrentUser.ToString())
        print([p.Id for p in app.PatientSummaries])

    finally:
        app.Dispose()

if __name__ == "__main__":
    main()
