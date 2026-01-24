"""Pattern: Facade
Category: Structural
Problem it solves: Provides a simplified interface to a complex subsystem.
When to use: You want to hide complexity behind a simple API.
When not to use: The subsystem is already simple or needs full control.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class VersionControlSystem(ABC):
    
    def pull_requests(self) -> str:
        print("Fetching pull requests from remote repository...")
    
class BuildSystem():
    def compile_code(self) -> str:
        print("Compiling the source code...")
    
    def get_artifact(self) -> str:
        print("Getting the build artifact...")
    
class TestingFramework():
    def run_unit_tests(self) -> str:
        print("Running unit tests...")
    
    def run_integration_tests(self) -> str:
        print("Running integration tests...")
    
class DeploymentTraget():
    def deploy(self) -> str:
        print("Deploying the application to the target environment...")
    
    def fetch_new_version(self) -> str:
        print("Fetching the new version of the application...")

class DeploymentFacade:
    def __init__(self):
        self.vcs = VersionControlSystem()
        self.build_system = BuildSystem()
        self.testing_framework = TestingFramework()
        self.deployment_target = DeploymentTraget()
    
    def deploy_new_version(self) -> str:
        print("Starting deployment of new version...")
        success = True
        try:
            self.vcs.pull_requests()
            self.build_system.compile_code()
            self.build_system.get_artifact()
            self.testing_framework.run_unit_tests()
            self.testing_framework.run_integration_tests()
            self.deployment_target.fetch_new_version()
            self.deployment_target.deploy()
        except Exception as e:
            success = False
            print(f"Deployment failed: {e}")
        if success:
            print("Deployment completed successfully.")
        
        return success

class DeploymentClient:
    def __init__(self, facade: DeploymentFacade):
        self.facade = facade
    
    def deploy(self):
        self.facade.deploy_new_version()
    print("Demo: Facade Pattern - Deployment Process")
    
if __name__ == "__main__":
    facade = DeploymentFacade()
    client = DeploymentClient(facade)
    client.deploy()