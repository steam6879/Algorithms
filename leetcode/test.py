from collections import defaultdict

def topological_sort_kahn(graph):
    indegree = defaultdict(int) # Track indegrees
    queue = [] #Initialize queue

    # Calculate indegrees
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    # Add nodes with 0 indegree to queue
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    topological_order = []

    # Process until queue is empty
    while queue:

        # Remove node from queue and add to topological order
        node = queue.pop(0)
        topological_order.append(node)

        # Reduce indegree for its neighbors
        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            # Add new 0 indegree nodes to queue
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(topological_order) != len(graph):
        print("Cycle exists")

    print(topological_order)

topological_sort_kahn(graph)


from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize a graph using a dictionary to map each course to its list of dependent courses
        graph = defaultdict(list)
      
        # Initialize a list to count incoming edges (prerequisites) for each course
        incoming_edges_count = [0] * num_courses
      
        # Build the graph and update the count of incoming edges for each course
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            incoming_edges_count[course] += 1
      
        # List to store the course order
        course_order = []
      
        # Queue to manage the courses with no incoming edges (no prerequisites)
        queue = deque(course for course, count in enumerate(incoming_edges_count) if count == 0)
      
        # Process the courses using a topological sort via BFS (Breadth-First Search)
        while queue:
            current_course = queue.popleft()
            course_order.append(current_course) # add the current course to the course order
          
            # Reduce the incoming edge count of dependent courses by 1
            for dependent_course in graph[current_course]:
                incoming_edges_count[dependent_course] -= 1
              
                # If a dependent course now has no incoming edges, add it to the queue
                if incoming_edges_count[dependent_course] == 0:
                    queue.append(dependent_course)
      
        # Check if the number of courses in the order list matches the total number of courses
        # If not, it means not all courses can be completed (cycle detected)
        return course_order if len(course_order) == num_courses else []
    

    from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct the graph
        graph = defaultdict(list)
        incoming_edges = [0] * numCourses
        
        for u, v in prerequisites:
            graph[v].append(u)
            incoming_edges[u] += 1
            
        # Add nodes with incoming edge count = 0 to the queue
        queue = deque([])
        for i in range(numCourses):
            if incoming_edges[i] == 0:
                queue.append(i)
                
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for adjacent_node in graph[node]:
                incoming_edges[adjacent_node] -= 1
                
                if incoming_edges[adjacent_node] == 0:
                    queue.append(adjacent_node)
                    
        if len(result) != numCourses:
            return []
        
        return result