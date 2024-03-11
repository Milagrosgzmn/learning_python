""" 
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
  """

play = [['piedra','papel'], ['piedra','tijera'], ['lagarto','papel'], ['piedra','lagarto'], ['spock','papel'], ['tijera','papel']]

def moreWins(games):

    def compare(round):
        if round[0]=='piedra':
            if round[1]== 'papel' or round[1] == 'spock':
                return 'player2'
            
            return 'player1'
        if round[0]=='papel':
            if round[1]== 'tijera' or round[1] == 'lagarto':
                return 'player2'
            
            return 'player1'
        if round[0]=='tijera':
            if round[1]== 'piedra' or round[1] == 'spock':
                return 'player2'
            
            return 'player1'
        if round[0]=='lagarto':
            if round[1]== 'tijera' or round[1] == 'piedra':
                return 'player2'
            
            return 'player1'
        if round[0]=='spock':
            if round[1]== 'papel' or round[1] == 'lagarto':
                return 'player2'
            
            return 'player1'

    winners = map(compare, games)

    player2Wins = filter( lambda winner: winner=='player2', winners)

    round_played= len(list(winners))
    
    if len(list(player2Wins))>round_played/2:
        return 'Player 2'
    elif len(list(player2Wins))==round_played/2:
        return 'Tie'
    else:
        return 'Player 1'



print(moreWins(play))

