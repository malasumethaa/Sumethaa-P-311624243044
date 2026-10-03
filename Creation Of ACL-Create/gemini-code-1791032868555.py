class ACLCreateManager:
    def __init__(self, roles_file="roles_registry.json", table_file="records_table.json"):
        self.roles_file = roles_file
        self.table_file = table_file

    def create_record(self, user_role, user_email, new_content):
        """Milestone 4: Validates permission and creates a new record if allowed[cite: 1]."""
        with open(self.roles_file, 'r') as f:
            roles = json.load(f)
            
        if not roles.get(user_role.upper(), {}).get("can_create", False):
            print(f"ACL CREATE denied for user {user_email} with role {user_role}.")
            return False
            
        with open(self.table_file, 'r') as f:
            table_data = json.load(f)
            
        new_record = {
            "record_id": f"REC-{len(table_data['records']) + 101}",
            "owner_email": user_email,
            "content": new_content,
            "created_at": datetime.now().isoformat()
        }
        
        table_data['records'].append(new_record)
        with open(self.table_file, 'w') as f:
            json.dump(table_data, f, indent=4)
            
        print(f"ACL CREATE success: New record added by {user_email}[cite: 1].")
        return True