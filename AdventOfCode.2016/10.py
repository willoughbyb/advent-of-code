import re

r_gives = re.compile(r'(low|high) to (bot|output) (\d+)')


def goes_to(line):
    line = line.split()
    bot_id = line[5]
    value = int(line[1])

    give_bot(bot_id, value)


def gives(line):
    instructions = r_gives.findall(line)
    bot_id = line.split()[1]

    val_min = min(bots[bot_id])
    val_max = max(bots[bot_id])

    if val_min == 17 and val_max == 61:
        print(' 17 compared with 61 found: {}'.format(bot_id))
        # quit()

    for instruction in instructions:
        if instruction[0] == 'low':
            value = val_min
        elif instruction[0] == 'high':
            value = val_max
        else:
            print('unknown instruction {}'.format(line))

        bots[bot_id].remove(value)

        if instruction[1] == 'bot':
            receive_id = instruction[2]
            give_bot(receive_id, value)
        elif instruction[1] == 'output':
            receive_id = instruction[2]
            give_output(receive_id, value)


def give_bot(bot_id, value):
    if bot_id not in bots.keys():
        bots[bot_id] = []

    if bot_id in watchlist:
        print('{} has received a value {}'.format(bot_id, value))

    if len(bots[bot_id]) > 2:
        print('bot {} already has 2 values!'.format(bot_id))
        quit()

    # print('  giving BOT {} {} - {}'.format(bot_id, value, bots[bot_id]))
    bots[bot_id].append(value)


def give_output(output_id, value):
    if output_id not in outputs.keys():
        outputs[output_id] = []

    print('  giving OUT {} {} - {}'.format(output_id,
                                           value, outputs[output_id]))
    outputs[output_id].append(value)


with open('10.input') as f:
    lines = f.read().split('\n')

bots = {}
outputs = {}

# list of the only bots who give anything to any output
watchlist = ['194', '18', '169', '67', '159', '43', '78', '186', '30',
             '165', '175', '60', '152', '74', '196', '158', '57', '104', '5', '97', ]

for line in lines:
    if ' goes to ' in line:
        goes_to(line)
        lines.remove(line)


while True:
    relevant_bots = [bot_entry for bot_entry in bots.items()
                     if len(bot_entry[1]) >= 2]

    if len(relevant_bots) == 0:
        break

    for bot, values in relevant_bots:
        # print('  {} {}'.format(bot, values))
        if bot in watchlist:
            print(bot)

        pattern = re.compile(r'^bot {}\b'.format(bot))
        line = [line for line in lines if pattern.match(line)]
        # print(line)
        gives(line[0])

print(outputs)
