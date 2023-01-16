# Image watermarking using Python
## Introduction
This side project is to implement basic steganography with images. Encode the first `7-K` bits of the watermark into the last `K` bits of the target image. You can put these two files in folder `./src` and set the configurations in `./config`. For details, please refer to the comments in the codes.

## Workflow
1. Import watermark (A) and target (B) as numpy arrays.
2. Encode the first `7-K` bits of A into the last `K` bits of B.
3. Decode the last `K` bits of B and left-shift `7-K` bits to reconstruct the A.

## Input and Output
### Input Images
<table class="col2" border="0">
 <tr>
    <td><b style="font-size:16px">Target image</b></td>
    <td><b style="font-size:16px">Watermark image</b></td>
 </tr>
 <tr>
    <td><img src="./src/target.jpg"></img></td>
    <td><img src="./src/watermark.jpg"></img></td>
 </tr>
</table>

### Encoded Results
<table class="col3" border="0">
 <tr>
    <td><b style="font-size:16px">Encode to last 1 bit</b></td>
    <td><b style="font-size:16px">Encode to last 2 bits</b></td>
    <td><b style="font-size:16px">Encode to last 3 bits</b></td>
 </tr>
 <tr>
    <td><img src="./dest/encode_last_1_bits.jpg"></img></td>
    <td><img src="./dest/encode_last_2_bits.jpg"></img></td>
    <td><img src="./dest/encode_last_3_bits.jpg"></img></td>
 </tr>
</table>

### Decoded watermark
<table class="col3" border="0">
 <tr>
    <td><b style="font-size:16px">Decode from last 1 bit</b></td>
    <td><b style="font-size:16px">Decode from last 2 bits</b></td>
    <td><b style="font-size:16px">Decode from last 3 bits</b></td>
 </tr>
 <tr>
    <td><img src="./dest/decode_last_1_bits.jpg"></img></td>
    <td><img src="./dest/decode_last_2_bits.jpg"></img></td>
    <td><img src="./dest/decode_last_3_bits.jpg"></img></td>
 </tr>
</table>

It's easy to encode A to B. As more bits are encoded, the more it affects the quality of the target image. On the contrary, the fewer bits the watermarks are encoded, the lower the quality of it can be restored.


## Development Environment
```
Python 3.9.6
MacOS 12.6
```

## How to use it?
1. Install the dependencies
    ```shell
    pip install -r requirements.txt
    ```
2. Update the `config.py` if needed

3. Run the `main.py`
    ```shell
    python main.py
    ```

<style>

.col2 td {
    max-width:50%;
    width:50%;
}

.col3 td {
    max-width:33%;
    width:33%;
}

table {
    width:100%;
}

</style>