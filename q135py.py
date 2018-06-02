class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        children_number = len(ratings)
        forward_list = [0] * children_number
        backward_list = [0] * children_number

        for i in range(children_number):
            if i == 0:
                forward_list[i] = 1
            else:
                if ratings[i] > ratings[i-1]:
                    forward_list[i] = forward_list[i-1] + 1
                else:
                    forward_list[i] = 1
        for i in range(children_number-1,-1,-1):
            if i == children_number-1:
                backward_list[i] = 1
            else:
                if ratings[i] > ratings[i+1]:
                    backward_list[i] = backward_list[i+1] + 1
                else:
                    backward_list[i] = 1
        sum = 0
        for i in range(children_number):
            sum += max(forward_list[i], backward_list[i])

        return sum
