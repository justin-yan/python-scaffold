# Given a graph of tasks, calculate total time to process a given task
# assume dedupe on cycles and no parallel processing
from collections import namedtuple, deque
from typing import List

Task = namedtuple("Task", ["id", "time", "deps"])


def simple_timecalc(start: int, tasks: List[Task]) -> int:
    taskindex = {}
    for task in tasks:
        taskindex[task.id] = task

    needed_jobs = set()
    searchqueue = deque([taskindex[start]])
    while searchqueue:
        curtask = searchqueue.popleft()
        needed_jobs.add(curtask.id)
        for dep in curtask.deps:
            if dep not in needed_jobs:  # Skip job from being searched again if previously seen
                searchqueue.append(taskindex[dep])

    return sum([taskindex[id].time for id in needed_jobs])


if __name__ == "__main__":
    print(simple_timecalc(1, [Task(1, 20, [2, 3]), Task(2, 10, [4]), Task(3, 5, []), Task(4, 5, [])]))
