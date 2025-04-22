
# https://en.wikipedia.org/wiki/Vehicle_identification_number
def validate_VIN(vin: str):
	#! VIN numbers must be 17 characters long.
	if len(vin) != 17:
		return False
	wmi = vin[0:3]
	manufacturer = wmi[1]
	vehicle_type = wmi[2]

	# Vehicle Descriptor Section (VDS)
	vds = vin[3:7]
	
	# Check Digit - Used to verify the authenticity of the VIN based on a mathematical calculation of the other characters.
	check_digit = vin[8]

	# Model Year - A character (letter or number) that indicates the vehicle's model year.
	model_year = vin[9]

	# Plant Code - Indentifies the specific manufacturing plant where the vehicle was assembled.
	plant_code = vin[10]

	# Vehicle Identifier Section (VIS) - Sequential production number assigned to the vehicle on the assembly line.
	vis = vin[11:16]

	