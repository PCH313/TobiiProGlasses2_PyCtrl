# demo_connection.py : A demo code for connecting with the Tobii Pro Glasses 2
#
# Copyright (C) 2017  Davide De Tommaso
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

from tobiiglasses.tobiiglassescontroller import TobiiGlassesController

import sys
import time


def main():

	tobiiglasses = TobiiGlassesController()

	project_name = input("Please insert the project's name: ")
	project_id = tobiiglasses.create_project(project_name)

	participant_name = input("Please insert the participant's name: ")
	participant_id = tobiiglasses.create_participant(project_id, participant_name)

	calibration_id = tobiiglasses.create_calibration(project_id, participant_id)
	input("Put the calibration marker in front of the user, then press enter to calibrate")
	tobiiglasses.start_calibration(calibration_id)

	res = tobiiglasses.wait_until_is_calibrated(calibration_id)

	if res is False:
		print("Calibration failed!")
		exit(1)

	recording_id = tobiiglasses.create_recording(participant_id)
	input("Press enter to start recording")
	tobiiglasses.start_recording(recording_id)
	input("Press enter to stop recording")
	tobiiglasses.stop_recording(recording_id)
	res = tobiiglasses.wait_until_recording_is_done(recording_id)

	if res is False:
		print("Recording failed!")
		exit(1)


if __name__ == '__main__':
    main()
