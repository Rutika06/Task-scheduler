import heapq

# Task class representing a task with a priority
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Task(name='{self.name}', priority={self.priority})"


# TaskScheduler class implementing priority-based task scheduling
class TaskScheduler:
    def __init__(self):
        self.task_queue = []

    # Method to add a new task to the scheduler
    def add_task(self, task):
        heapq.heappush(self.task_queue, task)  # Adds task to the priority queue

    # Method to retrieve and execute the highest priority task
    def execute_next_task(self):
        if self.task_queue:
            task = heapq.heappop(self.task_queue)  # Retrieves and removes the highest priority task
            print(f"Executing task: {task.name}")
        else:
            print("No tasks left to execute.")


# Main function demonstrating the usage of TaskScheduler
if __name__ == "__main__":
    scheduler = TaskScheduler()  # Creates an instance of TaskScheduler

    # Adding tasks with different priorities
    scheduler.add_task(Task("Task 1", 3))
    scheduler.add_task(Task("Task 2", 1))
    scheduler.add_task(Task("Task 3", 2))

    # Executing tasks in priority order
    scheduler.execute_next_task()  # Task 2 (highest priority)
    scheduler.execute_next_task()  # Task 3
    scheduler.execute_next_task()  # Task 1
    scheduler.execute_next_task()  # No tasks left
