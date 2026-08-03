"""
Server Capacity Studio
----------------------
Main file for Server Capacity Planner.
"""

from server_capacity_planner import ServerCapacityPlanner


class ServerCapacityStudio:

    def __init__(self):

        self.planner = ServerCapacityPlanner()

    # ----------------------------------
    # Add Server
    # ----------------------------------
    def add_server(self):

        print("\n========== ADD SERVER ==========\n")

        name = input(
            "Server Name: "
        ).strip()

        total_cpu = float(
            input(
                "Total CPU Cores: "
            )
        )

        used_cpu = float(
            input(
                "Used CPU Cores: "
            )
        )

        total_ram = float(
            input(
                "Total RAM (GB): "
            )
        )

        used_ram = float(
            input(
                "Used RAM (GB): "
            )
        )

        total_storage = float(
            input(
                "Total Storage (GB): "
            )
        )

        used_storage = float(
            input(
                "Used Storage (GB): "
            )
        )

        server = self.planner.add_server(

            name,
            total_cpu,
            used_cpu,
            total_ram,
            used_ram,
            total_storage,
            used_storage

        )

        print("\nServer Added Successfully.")

        self.planner.display_server(server)

    # ----------------------------------
    # View Servers
    # ----------------------------------
    def view_servers(self):

        self.planner.display_servers()

    # ----------------------------------
    # Critical Servers
    # ----------------------------------
    def critical_servers(self):

        servers = self.planner.critical_servers()

        if not servers:

            print("\nNo critical servers found.")

            return

        print("\n========== CRITICAL SERVERS ==========\n")

        for server in servers:

            self.planner.display_server(server)

    # ----------------------------------
    # Healthy Servers
    # ----------------------------------
    def healthy_servers(self):

        servers = self.planner.healthy_servers()

        if not servers:

            print("\nNo healthy servers found.")

            return

        print("\n========== HEALTHY SERVERS ==========\n")

        for server in servers:

            self.planner.display_server(server)

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        self.planner.display_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("         SERVER CAPACITY PLANNER")
            print("=" * 60)

            print("1. Add Server")
            print("2. View Server Report")
            print("3. Healthy Servers")
            print("4. Critical Servers")
            print("5. Capacity Summary")
            print("6. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_server()

            elif choice == "2":

                self.view_servers()

            elif choice == "3":

                self.healthy_servers()

            elif choice == "4":

                self.critical_servers()

            elif choice == "5":

                self.summary()

            elif choice == "6":

                print(
                    "\nThank you for using Server Capacity Planner."
                )

                break

            else:

                print("\nInvalid choice.")


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = ServerCapacityStudio()

    studio.menu()
