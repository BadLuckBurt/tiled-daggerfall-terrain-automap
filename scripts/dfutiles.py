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
							tileData += '\t"TileBitfield": 1,\n'
							if tileLayer.cellAt(x, y).tile() != None:
								cell = tileLayer.cellAt(x, y)
								id = cell.tile().id()
								tileData += '\t"TextureRecord": ' + str(id) + ',\n'
								if cell.flippedHorizontally == True:
									id = id + 2147483648
									tileData += '\t"IsFlipped": true,\n'
								else:
									tileData += '\t"IsFlipped": false,\n'
								#if cell.flippedVertically == True:
								if cell.flippedAntiDiagonally == True:
									id = id + 1073741824
									tileData += '\t"IsRotated": true\n'
								else:
									tileData += '\t"IsRotated": false\n'
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