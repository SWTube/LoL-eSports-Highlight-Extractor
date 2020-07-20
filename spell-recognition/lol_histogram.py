import lol_spell_recognition

def compare_images_2(imgA: np.ndarray, imgB: np.ndarray) -> float:
    """
    Compare two images through histogram

    Args:
        imgA: image in video
        imgB: original image

    Returns:
        Similarity between two images

    Raises:
        None
    """
    assert isinstance(imgA, np.ndarray)
    assert isinstance(imgB, np.ndarray)
    # Convert to hsv
    hsv_a = cv.cvtColor(imgA, cv.COLOR_BGR2HSV)
    hsv_b = cv.cvtColor(imgB, cv.COLOR_BGR2HSV)

    # Calculate and Normalize histogram
    hist_a = cv.calcHist([hsv_a], [0], None, [256], [0, 256])
    cv.normalize(hist_a, hist_a, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    hist_b = cv.calcHist([hsv_b], [0], None, [256], [0, 256])
    cv.normalize(hist_b, hist_b, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    # Compare hist_a, hist_b
    a_b_comparison = cv.compareHist(hist_a, hist_b, 0)

    return a_b_comparison