import numpy as np
import cv2

#https://3dtv.at//knowhow/anaglyphcomparison_en.aspx
def make_true_anaglyph(left, right):
    out = np.zeros_like(left, dtype=np.uint8)
    l_r =  left[:,:,2]
    l_g =  left[:,:,1]
    l_b =  left[:,:,0]

    r_r = right[:,:,2]
    r_g = right[:,:,1]
    r_b = right[:,:,0]
   
    out[:,:,2] = (l_r * 0.299) + (l_g * 0.587) + (l_b * 0.114)
    out[:,:,0] = (r_r * 0.299) + (r_g * 0.587) + (r_b * 0.114)

    return out

def make_gray_anaglyph(left, right):
    out = np.zeros_like(left, dtype=np.uint8)
    l_r =  left[:,:,2]
    l_g =  left[:,:,1]
    l_b =  left[:,:,0]

    r_r = right[:,:,2]
    r_g = right[:,:,1]
    r_b = right[:,:,0]

    #bgr
    out[:,:,2] = (l_r * 0.299) + (l_g * 0.587) + (l_b * 0.114)
    out[:,:,1] = (r_r * 0.299) + (r_g * 0.587) + (r_b * 0.114)
    out[:,:,0] = (r_r * 0.299) + (r_g * 0.587) + (r_b * 0.114)

    return out

def make_color_anaglyph(left, right):
    out = np.zeros_like(left, dtype=np.uint8)
    l_r =  left[:,:,2]

    r_g = right[:,:,1]
    r_b = right[:,:,0]

    out[:,:,2] = l_r
    out[:,:,1] = r_g
    out[:,:,0] = r_b

    return out


def make_half_color_anaglyph(left, right):
    out = np.zeros_like(left, dtype=np.uint8)

    l_r =  left[:,:,2]
    l_g =  left[:,:,1]
    l_b =  left[:,:,0]

    r_g = right[:,:,1]
    r_b = right[:,:,0]

    out[:,:,2] = (l_r * 0.299) + (l_g * 0.587) + (l_b * 0.114)
    out[:,:,1] = r_g
    out[:,:,0] = r_b

    return out

def make_optimized_anaglyph(left, right):
    out = np.zeros_like(left, dtype=np.uint8)

    l_g =  left[:,:,1]
    l_b =  left[:,:,0]

    r_g = right[:,:,1]
    r_b = right[:,:,0]

    out[:,:,2] = (l_g * 0.7) + (l_b * 0.3)
    out[:,:,1] = r_g
    out[:,:,0] = r_b

    return out


frame = cv2.imread('./imgs/file.jpg')

l_frame = frame[:, :640]
r_frame = frame[:, 640:]

l_frame = cv2.resize(l_frame, (1280, 960), interpolation= cv2.INTER_LINEAR)
r_frame = cv2.resize(r_frame, (1280, 960), interpolation= cv2.INTER_LINEAR)

true_anaglyph = make_true_anaglyph(left=l_frame, right=r_frame)

cv2.imwrite('./imgs/true_anaglyph.png', true_anaglyph)