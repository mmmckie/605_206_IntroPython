'''
This module defines the PlayoffElimination class. When executed as a script, it
will process 4 input files and check each team for playoff eligibility.
'''

import networkx as nx

class PlayoffElimination:
    
    def __init__(self, input_file: str):
        # Read input file and store each row of data in a list
        with open(input_file, 'r') as f:
            data = f.readlines()

        # Total number of teams is first row of data
        self.n_teams = int(data[0].strip())

        # Data for each team will be stored in these dicts
        self.team_name_mapping = {}
        self.wins = {}
        self.losses = {}
        self.remaining = {}
        self.games = {}
        
        # Parse each row of data in the input file
        for i in range(self.n_teams):
            # Split row into list for ease of indexing values
            row = data[i+1].split()
            # Grab team name, wins, losses, remaining total games, and remaining
            # games with every other team, then store in above dicts
            team_name = row[0]
            self.team_name_mapping[i] = team_name
            self.wins[i] = int(row[1])
            self.losses[i] = int(row[2])
            self.remaining[i] = int(row[3])
            self.games[i] = {}
            for n in range(self.n_teams):
                self.games[i][n] = int(row[n+4])
    
    def create_flow_graph(self, team: int):
        '''Construct a graph to simulate the flow of potential wins for each team.'''

        # Create lists for all other teams and all other team combinations
        # These will be the team nodes and game nodes for the flow graph
        other_teams = []
        other_team_combos = []

        for i in range(self.n_teams):
            # Skip adding the team under consideration to the team nodes
            if i != team:
                other_teams.append(i)

            for j in range(i+1, self.n_teams):
                # Skip games involving the team under consideration
                if i != team and j != team:
                    other_team_combos.append((i, j))
        
        # Creating directed graph to represent flow of potential wins
        graph = nx.DiGraph()
        
        # Adding source node, game nodes, team nodes, and sink node
        graph.add_node('s')
        graph.add_nodes_from(other_team_combos)
        graph.add_nodes_from(other_teams)
        graph.add_node('t')

        # Creating empty lists to store all edges that will be added to the graph
        remaining_game_edges = []
        win_edges = []
        final_edges = []

        for game in other_team_combos:
            # Remaining number of games between (Team1, Team2) in 'game'
            games_left = self.games[game[0]][game[1]]
            
            # Adding edge from source to (Team1, Team2) with weight = games_left
            remaining_game_edges.append(('s', game, {'games': games_left}))

            # Generating edges from each team combination to each individual
            # team and setting their weights to infinity
            for each_team in game:
                win_edges.append((game, each_team, {'games': float('inf')}))

        # Add both lists of edges to the graph
        graph.add_edges_from(remaining_game_edges)
        graph.add_edges_from(win_edges)

        # Now for each of the individual team nodes, create edge from that node
        # to the sink node - weight is max number of games that team can win
        # without eliminating the team under consideration
        for node in other_teams:
            weight = self.wins[team] + self.remaining[team] - self.wins[node]
            final_edges.append((node, 't', {'games': weight}))
        
        # Add these edges to the flow graph and return the graph
        graph.add_edges_from(final_edges)
        return graph

    def max_flow_elimination(self, team: int):
        '''
        Generate flow graph for 'team' and then compute the max flow to check
        if max flow is less than the total number of games left to be played.
        
        Arguments:
        team: int = team under consideration for playoff eligibility

        Returns:
        eliminated: boolean = True if the max flow is less than the number of
            games left to be played between other teams. False otherwise.
        '''

        # First create the flow graph, then compute the max flow
        graph = self.create_flow_graph(team)
        max_flow = nx.maximum_flow_value(graph,
                                         _s = 's',
                                         _t = 't',
                                         capacity='games')
        
        # Getting the total number of remaining games left for every other team
        # to play - this will equal the sum of the capacities to the game nodes
        total_games = 0
        for i in range(self.n_teams):
            for j in range(i+1, self.n_teams):
                # Making sure to exclude games that the current team is in
                if i != team and j != team:
                    total_games += self.games[i][j]
        
        if max_flow < total_games:
            eliminated = True
        else:
            eliminated = False
        
        return eliminated

    def determine_elimination_status(self):
        '''Checks if each team is trivially eliminated, and if not, uses the max
        flow to determine elimination status.'''

        # Get the team with the highest current wins to check for trivial elims
        most_wins = max(self.wins.values())
        for team in self.wins:
            if self.wins[team] == most_wins:
                frontrunner = self.team_name_mapping[team]
                # If the frontrunner is found, no need to check the other teams
                break

        # Iterate through all teams
        for team in self.wins:
            team_name = self.team_name_mapping[team]

            # First check for trivial elimination
            max_possible_wins = self.wins[team] + self.remaining[team]
            if max_possible_wins < most_wins:
                print(f'{team_name} has been trivially eliminated by {frontrunner}.')
            
            else:
                # If not trivially eliminated, use max flow algorithm to check
                # for elimination
                eliminated = self.max_flow_elimination(team)
                
                # And print results
                if eliminated:
                    print(f'{team_name} has been eliminated.')
                else:
                    print(f'{team_name} is not eliminated.')


def main():
    input_files = ['potter.txt', 'mlb.txt', 'ivy_league.txt', 'world_cup.txt']
    for file in input_files:
        # Instantiate PlayoffElimination class and run elimination simulation
        elimination_checker = PlayoffElimination(file)
        elimination_checker.determine_elimination_status()
        #Adding a line of whitespace between outputs of each file
        print()


if __name__ == '__main__':
    main()
