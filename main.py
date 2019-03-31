if __name__ == '__main__':


def mathingMap(img, template):
    rows,cols = img.shape
    trows,tcols = template.shape
    matching_map = np.zeros(rows-trows+1,cols-tcols+1)

    