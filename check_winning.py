def check_winnings(columns,lines,bet,value):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][lines]
        for column in columns:
            symbol_to_check =column[lines]
            if symbol != symbol_to_check:
                break
        else:
            winnings+= value[symbol] *bet
            winning_lines.append(line+1)


    return winnings,winning_lines