#############################################
##       Load livingRoom wordMap
#############################################
print('Load livingRoom wordMap')

rawFiles = '/smartRemotes/nodes/irNode/zones/livingRoom/'

wordMap = {
	
	"Softer": [
		{"controlWord": "Softer", "rawFile": rawFiles + "softer.raw", "deviceCommand": "necx:0x80d988"}
	],
	
	"Louder": [
		{"controlWord": "Louder", "rawFile": rawFiles + "louder.raw", "deviceCommand": "necx:0x80d98a"}
	],
	
	"Silence": [
		{"controlWord": "Silence", "rawFile": rawFiles + "soundToggle.raw", "deviceCommand": "necx:0x80d98c"}
	],
	
	"Sound": [
		{"controlWord": "Sound", "rawFile": rawFiles + "soundToggle.raw", "deviceCommand": "necx:0x80d98c"}
	],
	
	"SoundToggle": [
		{"controlWord": "SoundToggle", "rawFile": rawFiles + "soundToggle.raw", "deviceCommand": "necx:0x80d98c"}
	],
    
	"Off": [
		{"controlWord": "Off", "rawFile": rawFiles + "powerToggle.raw", "deviceCommand": "necx:0x86050f"}
	],
    
	"On": [
		{"controlWord": "On", "rawFile": rawFiles + "powerToggle.raw", "deviceCommand": "necx:0x86050f"}
	],
    
	"PowerToggle": [
		{"controlWord": "PowerToggle", "rawFile": rawFiles + "powerToggle.raw", "deviceCommand": "necx:0x86050f"}
	],
}