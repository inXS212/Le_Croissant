import math

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from LeFramework.common.Objs import *
from LeFramework.common.Areas import *
from LeFramework.common.Vector import *
from LeFramework.common.ConstVec import *
from States import *
from Controllers import *

class LeCroissant2(BaseAgent):
	def initialize_agent(self):
		self.me = Car(self.index)
		self.ball = Ball()
		#This runs once before the bot starts up
		self.controller_state = SimpleControllerState()
		self.bma = BallMetaArea()

		self.start = 0.0
		self.state = RandPatrol()
		self.controller = controller

	def preprocess(self,game):
		# print(game)
		self.time = game.game_info.seconds_elapsed
		self.me.process(game.game_cars[self.index])
		self.ball.process(game.game_ball)
		self.bma.update(self.ball, self.team)

	def print_out(self):
		# print(self.bma.inShotZone(self.me.loc))
		pass

	def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
		self.preprocess(packet)
		self.render()
		self.print_out()
		return self.state.execute(self)

	def render(self):
		self.renderer.begin_rendering()
		# self.renderer.draw_line_3d(self.ball.loc.vec,ConstVec.get('Home_L',self.me.team).vec, self.renderer.red())
		# self.renderer.draw_line_3d(self.ball.loc.vec,ConstVec.get('Home_R',self.me.team).vec, self.renderer.red())
		# self.renderer.draw_line_3d(self.ball.loc.vec,self.me.loc.vec, self.renderer.blue())
		# self.renderer.draw_line_3d(self.ball.loc.vec,self.bma.Home_sideL.vec, self.renderer.blue())
		# self.renderer.draw_line_3d(self.ball.loc.vec,self.bma.Home_sideR.vec, self.renderer.blue())
		self.renderer.end_rendering()


# class Vector2:
# 	def __init__(self, x=0, y=0):
# 		self.x = float(x)
# 		self.y = float(y)

# 	def __add__(self, val):
# 		return Vector2(self.x + val.x, self.y + val.y)

# 	def __sub__(self, val):
# 		return Vector2(self.x - val.x, self.y - val.y)

# 	def correction_to(self, ideal):
# 		# The in-game axes are left handed, so use -x
# 		current_in_radians = math.atan2(self.y, -self.x)
# 		ideal_in_radians = math.atan2(ideal.y, -ideal.x)

# 		correction = ideal_in_radians - current_in_radians

# 		# Make sure we go the 'short way'
# 		if abs(correction) > math.pi:
# 			if correction < 0:
# 				correction += 2 * math.pi
# 			else:
# 				correction -= 2 * math.pi

# 		return correction

# def get_car_facing_vector(car):
# 	pitch = float(car.physics.rotation.pitch)
# 	yaw = float(car.physics.rotation.yaw)

# 	facing_x = math.cos(pitch) * math.cos(yaw)
# 	facing_y = math.cos(pitch) * math.sin(yaw)

# 	return Vector2(facing_x, facing_y)