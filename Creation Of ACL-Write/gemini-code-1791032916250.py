class ACLWriteManager:
    def __init__(self, roles_file="roles_registry.json", table_file="records_table.json"):
        self.roles_file = roles_file
        self.table_file = table_file

    def update_record(self, user_role, user_email, record_id, updated_content):
        """Milestone 5: Validates and updates an existing record[cite: 1]."""
        with open(self.roles_file, 'r') as f:
            roles = json.load(f)
            
        if not roles.get(user_role.upper(), {}).get("can_write", False):
            print(f"ACL WRITE denied for user {user_email}.")
            return False
            
        with open(self.table_file, 'r') as f:
            table_data = json.load(f)
            
        record_found = False
        for rec in table_data['records']:
            if rec['record_id'] == record_id:
                rec['content'] = updated_content
                rec['last_modified_by'] = user_email
                record_found = True
                break
                
        if record_found:
            with open(self.table_file, 'w') as f:
                json.dump(table_data, f, indent=4)
            print(f"ACL WRITE success: Record {record_id} updated[cite: 1].")
            return True
        
        print("Record ID not found.")
        return False