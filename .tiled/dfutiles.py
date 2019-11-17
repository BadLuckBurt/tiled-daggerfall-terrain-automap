from tiled import *

class DfuTiles(Plugin):
	@classmethod
	def nameFilter(cls):
		return "DFU JSON tiles (*.json)"

	@classmethod
	def shortName(cls):
		return "dfutiles"

	@classmethod
	def write(cls, tileMap, fileName):
		with open(fileName, 'w') as fileHandle:
			for i in range(tileMap.layerCount()):
				if isTileLayerAt(tileMap, i):
					tileLayer = tileLayerAt(tileMap, i)
					for y in range(tileLayer.height()):
						tiles = []
						for x in range(tileLayer.width()):
							tileData = '{\n'
							if tileLayer.cellAt(x, y).tile() != None:
								cell = tileLayer.cellAt(x, y)
								id = cell.tile().id()
								bitfield = id
								if (cell.flippedHorizontally == True):
									bitfield |= 0x80
								if (cell.flippedAntiDiagonally == True):
									bitfield |= 0x40
								tileData += '\t"TileBitfield": ' + str(bitfield) + ',\n'
								tileData += '\t"TextureRecord": ' + str(id) + ',\n'
								if cell.flippedHorizontally == True:
									tileData += '\t"IsFlipped": true\n'
								else:
									tileData += '\t"IsFlipped": false\n'
								if cell.flippedAntiDiagonally == True:
									tileData += '\t"IsRotated": true,\n'
								else:
									tileData += '\t"IsRotated": false,\n'
								tileData += '}'
								tiles.append(tileData)
							else:
								tiles.append(str(-1))
						line = ',\n'.join(tiles)
						if y == tileLayer.height() - 1:
							line += ''
						else:
							line += ','
						print(line, file=fileHandle)


		return True