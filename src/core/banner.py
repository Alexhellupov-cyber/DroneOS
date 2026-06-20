class Banner:

    def show(self, app_name: str, version: str):
        print("=" * 50)
        print(f"{app_name} v{version}")
        print("=" * 50)