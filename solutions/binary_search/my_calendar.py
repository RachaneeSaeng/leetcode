# https://leetcode.com/problems/my-calendar-i/description/
# https://algo.monster/liteproblems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.calendar = []
        
    def getTargetInsertionIdex(self, startTime: int) -> int:
        # find the first item that end time < starttime
        left, right = 0, len(self.calendar)-1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            _, end = self.calendar[mid]
            if end <= startTime:
                 result = mid
                 left = mid + 1
            else:
                right = mid - 1
            
        return result + 1
    
    def book(self, startTime: int, endTime: int) -> bool:
        targetInsertionIndex = self.getTargetInsertionIdex(startTime)        
        
        if targetInsertionIndex < len(self.calendar):
            next_start,_ = self.calendar[targetInsertionIndex] 
            if endTime > next_start:
                return False
                
        self.calendar.insert(targetInsertionIndex, (startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)