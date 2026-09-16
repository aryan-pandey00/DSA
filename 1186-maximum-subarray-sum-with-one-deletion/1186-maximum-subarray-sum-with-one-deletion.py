class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodelete = arr[0]
        onedelete = float('-inf')# One deletion not possible at start, 1 elemnt is present only 
        result = arr[0]

        for i in range(1, len(arr)):
            prev_nodelete = nodelete
            prev_onedelete = onedelete

            # No deletion: extend or start new
            nodelete = max(prev_nodelete + arr[i], arr[i])

            # Delete current OR deletion already used
            onedelete = max(prev_nodelete, prev_onedelete + arr[i])

            # Update overall maximum
            result = max(result, nodelete, onedelete)

        return result