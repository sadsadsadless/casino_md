import flask
import flask_cors

import gen
import table

class TableRuler:
    def __init__(
            self
    ):
        self.tables = []
        self.tableData = gen.generate()
        for tableInst in self.tableData['Tables']:
            self.tables.append(table.Table(tableInst['Type']))

    def getFreeSpaces(
            self
    ):
        freeSpaces = []
        for tableInd in range(len(self.tables)):
            for placeInd in range(len(self.tables[tableInd].places)):
                if self.tables[tableInd].places[placeInd] == table.free:
                    totalX = self.tableData['Tables'][tableInd]['playerPlaces'][placeInd]['x'] + self.tableData['Tables'][tableInd]['Location']['x']
                    totalY = self.tableData['Tables'][tableInd]['playerPlaces'][placeInd]['y'] + self.tableData['Tables'][tableInd]['Location']['y']
                    freeSpaces.append({'x': totalX, 'y': totalY, 'table': tableInd, 'place': placeInd})

        return freeSpaces

    def unlockTable(
            self,
            tableInd,
            placeInd
    ):
        self.tables[tableInd].places[placeInd] = table.free

if __name__ == '__main__':
    tr = TableRuler()

    app = flask.Flask('table')
    flask_cors.CORS(app)

    @app.route('/get_free_spaces')
    def get_free_spaces():
        print('someone got places')
        return {'places': tr.getFreeSpaces()}

    @app.route('/sit_at_place')
    def sit_at_place():
        tableInd = int(flask.request.args.get('table', 0))
        placeInd = int(flask.request.args.get('place', 0))
        print(f'someone sit at place {tableInd},{placeInd}')
        return str(tr.tables[tableInd].trySit(placeInd))

    @app.route('/try_play')
    def try_play():
        tableInd = int(flask.request.args.get('table', 0))
        placeInd = int(flask.request.args.get('place', 0))
        name = flask.request.args.get('name', '')
        money = int(flask.request.args.get('money', 0))
        toRet = tr.tables[tableInd].tryPlay(placeInd, money, name)
        return str(int(toRet))

    @app.route('/unlock_table')
    def unlock_table():
        tableInd = int(flask.request.args.get('table', 0))
        placeInd = int(flask.request.args.get('place', 0))
        print(f'unlocked table {tableInd},{placeInd}')
        tr.unlockTable(tableInd, placeInd)
        return 'ok'




    app.run(port=5007, debug=True)