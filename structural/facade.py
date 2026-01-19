"""Pattern: Facade
Category: Structural
Problem it solves: Provides a simplified interface to a complex subsystem.
When to use: You want to hide complexity behind a simple API.
When not to use: The subsystem is already simple or needs full control.
"""


class AuthService:
    def authenticate(self, userid, user_pass):
        return f"Loggedin User: {userid}"

class TokenService:
    def issue_token(self, userid):
        return f"token for user: {userid} is usertoken::123"

class PermissionService:
    def has_permission(self, userid, resource):
        return f"user: {userid}, has access to dashboard"

class NotificationService:
    def send_login_alert(self, userid):
        print(f"[Notify] login alert sent to {userid}")

class SecurityFacade:
    
    def __init__(self):
        self.auth = AuthService()
        self.token = TokenService()
        self.perms = PermissionService()
        self.notify = NotificationService()
        
    def login(self, userid, password, resource):
        if not self.auth.authenticate(userid,password):
            return False
        
        if not self.perms.has_permission(userid, resource):
            return False
        
        self.notify.send_login_alert(userid)
        return self.token.issue_token(userid)
    
def demo():
    facade = SecurityFacade()
    token = facade.login("user1", "password", "dashboard")
    print(token)
if __name__ == "__main__":
    demo()
            
        
    
    