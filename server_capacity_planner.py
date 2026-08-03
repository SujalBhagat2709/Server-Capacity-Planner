"""
Server Capacity Planner
-----------------------
File : server_capacity_planner.py

Features
--------
✔ Add Server
✔ CPU Capacity Tracking
✔ RAM Capacity Tracking
✔ Storage Capacity Tracking
✔ Resource Utilization
✔ Remaining Capacity
✔ Server Status
✔ Capacity Summary
"""


class ServerCapacityPlanner:

    def __init__(self):

        self.servers = []

    # ----------------------------------
    # Utilization Percentage
    # ----------------------------------
    def utilization(self,
                    used,
                    total):

        if total == 0:

            return 0

        return round(

            (used / total) * 100,

            2

        )

    # ----------------------------------
    # Remaining Capacity
    # ----------------------------------
    def remaining(self,
                  total,
                  used):

        return total - used

    # ----------------------------------
    # Server Status
    # ----------------------------------
    def server_status(self,
                      cpu_percent,
                      ram_percent,
                      storage_percent):

        highest = max(

            cpu_percent,
            ram_percent,
            storage_percent

        )

        if highest >= 90:

            return "Critical"

        elif highest >= 75:

            return "High Usage"

        elif highest >= 50:

            return "Moderate"

        return "Healthy"

    # ----------------------------------
    # Add Server
    # ----------------------------------
    def add_server(self,
                   server_name,
                   total_cpu,
                   used_cpu,
                   total_ram,
                   used_ram,
                   total_storage,
                   used_storage):

        cpu_percent = self.utilization(
            used_cpu,
            total_cpu
        )

        ram_percent = self.utilization(
            used_ram,
            total_ram
        )

        storage_percent = self.utilization(
            used_storage,
            total_storage
        )

        server = {

            "Server": server_name,

            "CPU %":
                cpu_percent,

            "RAM %":
                ram_percent,

            "Storage %":
                storage_percent,

            "CPU Remaining":
                self.remaining(
                    total_cpu,
                    used_cpu
                ),

            "RAM Remaining":
                self.remaining(
                    total_ram,
                    used_ram
                ),

            "Storage Remaining":
                self.remaining(
                    total_storage,
                    used_storage
                ),

            "Status":
                self.server_status(
                    cpu_percent,
                    ram_percent,
                    storage_percent
                )

        }

        self.servers.append(server)

        return server

    # ----------------------------------
    # Healthy Servers
    # ----------------------------------
    def healthy_servers(self):

        return [

            server

            for server in self.servers

            if server["Status"] == "Healthy"

        ]

    # ----------------------------------
    # Critical Servers
    # ----------------------------------
    def critical_servers(self):

        return [

            server

            for server in self.servers

            if server["Status"] == "Critical"

        ]

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        return {

            "Total Servers":
                len(self.servers),

            "Healthy":
                len(
                    self.healthy_servers()
                ),

            "Critical":
                len(
                    self.critical_servers()
                ),

            "Average CPU %":
                round(

                    sum(

                        server["CPU %"]

                        for server in self.servers

                    )

                    / len(self.servers),

                    2

                ) if self.servers else 0

        }

    # ----------------------------------
    # Display Server
    # ----------------------------------
    def display_server(self,
                       server):

        print("\n========== SERVER ==========\n")

        for key, value in server.items():

            print(f"{key:<22}: {value}")

    # ----------------------------------
    # Display All Servers
    # ----------------------------------
    def display_servers(self):

        if not self.servers:

            print("\nNo server records found.")

            return

        print("\n========== SERVER REPORT ==========\n")

        for index, server in enumerate(

                self.servers,
                start=1):

            print(f"Server {index}")

            print("-" * 40)

            for key, value in server.items():

                print(f"{key:<22}: {value}")

            print()

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print("\n========== SUMMARY ==========\n")

        for key, value in report.items():

            print(f"{key:<22}: {value}")


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    planner = ServerCapacityPlanner()

    while True:

        print("\n1. Add Server")
        print("2. View Server Report")
        print("3. Capacity Summary")
        print("4. Critical Servers")
        print("5. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            name = input(
                "Server Name: "
            )

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

            server = planner.add_server(

                name,
                total_cpu,
                used_cpu,
                total_ram,
                used_ram,
                total_storage,
                used_storage

            )

            planner.display_server(server)

        elif choice == "2":

            planner.display_servers()

        elif choice == "3":

            planner.display_summary()

        elif choice == "4":

            servers = planner.critical_servers()

            if servers:

                for server in servers:

                    planner.display_server(
                        server
                    )

            else:

                print(
                    "\nNo critical servers."
                )

        elif choice == "5":

            print(
                "\nThank you for using Server Capacity Planner."
            )

            break

        else:

            print("\nInvalid choice.")
