class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches and sandwiches[0] in students:
            students.remove(sandwiches[0])
            sandwiches.pop(0)
    
        return len(students)     