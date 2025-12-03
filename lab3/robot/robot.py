from context import *

class Found(Exception):
    """
    This class is raised when a robot finds the goal.
    """
    pass

class Robot(object):

    def __init__(self, context):
        """
        Creates a robot with given context.
        :param context: the context of the robot
        """
        self.context = context


    def reachable(self, direction):
        """
        Checks if the robot can reach the neighbor cell
        :param direction: the direction of the neighbor cell
        """
        return self.context.reachable(direction)

    def move(self, direction):
        """
        Moves the robot to the neighbor cell of the given direction
        :param direction: the direction of the neighbor cell
        """
        self.context.move(direction)

    def findgoal(self):
        """
        Moves the robot until it finds the goal.
        The robot must print out all the steps
        it takes on its way
        """
        visited = set()

        def dfsMapDiscover(pos):
            if self.context.isgoal():
                raise Found()
            
            visited.add(pos)
            for direction in Direction:
                if self.reachable(direction):
                    new_pos = (pos[0] - (direction == Direction.NORTH) + (direction == Direction.SOUTH),
                               pos[1] + (direction == Direction.EAST) - (direction == Direction.WEST))
                    if new_pos not in visited:
                        self.move(direction)
                        print(f"Go {direction.name}")
                        dfsMapDiscover(new_pos)
                        print(f"Backtracking from {new_pos} to {pos}")

        try:
            start = (0, 0)
            dfsMapDiscover(start)
            print("Goal not reachable")
        except Found:
            print("Goal found!")

def main():
    r2d2 = Robot(context1)
    r2d2.findgoal()

if __name__ == "__main__":
    main()
