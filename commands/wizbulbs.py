from pywizlight import wizlight, PilotBuilder, discovery
import asyncio


async def turnOn():

    bulb = wizlight("192.168.8.145")

    await bulb.turn_on()
    print('włączono światło')
    state = await bulb.updateState()
    print(state.get_colortemp())
    print(state.get_rgb())


async def turnOff():

    bulb = wizlight("192.168.8.145")

    await bulb.turn_off()
    print('wyłączono światło')

async def setColor(text):

    bulb = wizlight("192.168.8.145")

    if('czerwony' in text):
        await bulb.turn_on(PilotBuilder(rgb = (255,0,0)))

    elif('niebieski' in text):
        await bulb.turn_on(PilotBuilder(rgb = (0,0,255)))

    elif('zielony' in text):
        await bulb.turn_on(PilotBuilder(rgb = (0,255,0)))

    elif('magenta' in text):
        await bulb.turn_on(PilotBuilder(rgb = (255,0,255)))

    elif('ciepły biały' in text):
        await bulb.turn_on(PilotBuilder(scene = 14))

    elif('biały' in text):
        await bulb.turn_on(PilotBuilder(scene = 12))

async def setColor(text):

    bulb = wizlight("192.168.8.145")

    await bulb.turn_on(PilotBuilder(brightness = 255))
