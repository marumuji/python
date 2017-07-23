def recall_password(grille, password):
    result = []
    rotate = grille
    for i in range(4):
        result.append("".join(read_password(rotate, password)))
        rotate = rotate_grille(rotate)
    print("".join(result))

def rotate_grille(grille):
    result = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            result[j][len(grille) - i - 1] = grille[i][j]
    return result

def read_password(grille, password):
    result = []
    for i in range(4):
        for j in range(4):
            if(grille[i][j] == "X"):
                result.append(password[i][j])
    return result




recall_password(
     ('X...',
      '..X.',
      'X..X',
      '....'),
     ('itdf',
      'gdce',
      'aton',
      'qrdi'))
# recall_password(
#     ('X...',
#      '..X.',
#      'X..X',
#      '....'),
#     ('itdf',
#      'gdce',
#      'aton',
#      'qrdi')) == 'icantforgetiddqd'
# ​
recall_password(
 ('....',
  'X..X',
  '.X..',
  '...X'),
 ('xhwc',
  'rsqx',
  'xqzz',
  'fyzr'))
# recall_password(
#     ('....',
#      'X..X',
#      '.X..',
#      '...X'),
#     ('xhwc',
#      'rsqx',
#      'xqzz',
#      'fyzr')) == 'rxqrwsfzxqxzhczy'
