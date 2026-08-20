from typing import List

# Contains various helper functions for graphics manipulation

# Standard procedures


def xflip_tiles(gfx_bytes: bytearray) -> bytearray:
    # Performs a horizontal flip operation on the tiles
    gfx_out = bytearray(len(gfx_bytes))
    for i in range(len(gfx_bytes)):
        temp = 0
        for j in range(8):  # horizontal flip this line
            invbit = 7 - j
            temp = temp + (((gfx_bytes[i]>>j)&1)<<invbit)
        gfx_out[i] = temp
    return gfx_out


def yflip_tiles(gfx_bytes: bytearray) -> bytearray:
    # Performs a vertical flip operation on the tiles
    # This is slightly complex due to how a typical SNES tile is arranged
    gfx_out = bytearray(len(gfx_bytes))
    num_tiles = len(gfx_bytes)>>4   # interpret as 2bpp tiles, since that's easier
    for i in range(num_tiles):
        temp = i<<4 # tile offset
        for j in range(8):
            tile_dex = 7-j
            tile_dex = tile_dex<<1
            orig_dex = j<<1
            gfx_out[temp+tile_dex] = gfx_bytes[temp+orig_dex]
            gfx_out[temp+tile_dex+1] = gfx_bytes[temp+orig_dex+1]
    return gfx_out


def lshift_tiles(gfx_bytes: bytearray, shift: int) -> bytearray:
    # Performs a "left shift" on the tiles (shifts pixels to the left)
    # Shift amount should be from 0-8
    gfx_out = bytearray(len(gfx_bytes))
    for i in range(len(gfx_bytes)):
        gfx_out[i] = (gfx_bytes[i]<<shift)&0xFF # clamp just in case
    return gfx_out


def rshift_tiles(gfx_bytes: bytearray, shift: int) -> bytearray:
    # Performs a "right shift" on the tiles (shifts pixels to the right)
    # Shift amount should be from 0-8
    gfx_out = bytearray(len(gfx_bytes))
    for i in range(len(gfx_bytes)):
        gfx_out[i] = (gfx_bytes[i]>>shift)&0xFF # clamp just in case
    return gfx_out


def rotleft_tiles(gfx_bytes: bytearray, rot: int) -> bytearray:
    # "Rotates" a tile leftwards by a certain amount
    # Rotation amount should be from 0-8
    gfx_out = bytearray(len(gfx_bytes))
    for i in range(len(gfx_bytes)):
        temp = (gfx_bytes[i]<<8)+(gfx_bytes[i])
        temp = (temp<<rot)>>8
        gfx_out[i] = temp&0xFF # clamp just in case
    return gfx_out


def rotright_tiles(gfx_bytes: bytearray, rot: int) -> bytearray:
    # "Rotates" a tile rightwards by a certain amount
    # Rotation amount should be from 0-8
    gfx_out = bytearray(len(gfx_bytes))
    for i in range(len(gfx_bytes)):
        temp = (gfx_bytes[i]<<8)+(gfx_bytes[i])
        temp = temp>>rot
        gfx_out[i] = temp&0xFF # clamp just in case
    return gfx_out


# Some stuff specifically for Pause Menu Text things


def conv_4bpp_to_1bpp(gfx_bytes: bytearray) -> bytearray:
    # We only care about the "first" byte of each pixel line here, so it should be an easy conversion
    num_tiles = len(gfx_bytes)>>5
    gfx_out = bytearray(num_tiles<<3)

    for i in range(8):
        for j in range(num_tiles):
            index = i<<1
            index = index + (j<<5)
            gfx_out[i+(j<<3)] = gfx_bytes[index]
    return gfx_out


def conv_1bpp_to_buffer(text_buffer: List[int], gfx_bytes: bytearray) -> List[int]:
    # Converts 1BPP 8x8 tiles into a "string" of 8 pixel lines
    num_tiles = len(gfx_bytes)>>3

    for i in range(8):  # 8 pixel lines
        for j in range(num_tiles):
            if j == 0:
                text_buffer[i] = gfx_bytes[j*8+i]
            else:
                text_buffer[i] = (text_buffer[i]<<8)+(gfx_bytes[j*8+i])
    return text_buffer


def conv_buffer_to_1bpp(text_buffer: List[int], gfx_bytes: bytearray) -> bytearray:
    # Converts a "string" of 8 pixel lines into 1BPP 8x8 tiles
    num_tiles = len(gfx_bytes)>>3

    for i in range(8):  # 8 pixel lines
        for j in range(num_tiles):
            tile_dex = num_tiles-j-1  # tile index to copy to
            if j == 0:
                gfx_bytes[tile_dex*8+i] = text_buffer[i]&0xFF
            else:
                text_buffer[i] = text_buffer[i]>>8
                gfx_bytes[tile_dex*8+i] = text_buffer[i]&0xFF
    return gfx_bytes


def conv_1bpp_to_4bpp(gfx_bytes: bytearray) -> bytearray:
    # This is a little more complex due to how the SNES handles tiles
    # A 4bpp 8x8 tile is actually two 2bpp tiles next to each other
    num_tiles = len(gfx_bytes)>>3
    gfx_out = bytearray(num_tiles<<5)

    for i in range(8):
        for j in range(num_tiles):
            index = j<<5
            index = index + (i<<1)
            gfx_out[index] = gfx_bytes[i+j*8]
            gfx_out[index+1] = ~gfx_bytes[i+j*8]&0xff
            gfx_out[index+0x10] = 0
            gfx_out[index+0x11] = 0
    return gfx_out


def conv_1bpp_to_2bpp(gfx_bytes: bytearray) -> bytearray:
    # A 2bpp version for SMW, if we ever get to it...
    num_tiles = len(gfx_bytes)>>3
    gfx_out = bytearray(num_tiles<<4)

    for i in range(8):
        for j in range(num_tiles):
            index = j<<4
            index = index + (i<<1)
            gfx_out[index] = gfx_bytes[i+j*8]
            gfx_out[index+1] = ~gfx_bytes[i+j*8]
    return gfx_out

