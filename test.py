address = "F-7-417"
block, building, room = address.split("-")
floor = room[0]

print(f"Block: {block}, Building: {building}, Room: {room}, Floor: {floor}")