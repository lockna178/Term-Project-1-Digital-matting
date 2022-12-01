# Term-Project-1-Digital-matting

## Members - collaboration in group
### Emma Rose Rorick 20191984
--> responsible for code organization/edit, document prep, research
### Polina Kotova 20191972
--> responsible for final code and video, masking blur, presentation prep
### Anastasia Gordeeva 20191186
--> responsible for code adjustments, extra research, document adjustments, etc.

## Our project 
Our core algorithm's goal is to, fundamentally, swap one defined color for another. This is the purpose of chroma-keying in modern video/photo editing. This code is an attempt at replicating a simple chromakey tool which can be found in Adobe After Effects, Premiere Pro, and so on. 

## Use explanation
1. Prepare source images / videos by defining:
  -width
  -height
  -fps
  -frames
  -image size
  -canvas
2. Define low and high color threshold to target (MUST be in HSV for most accurate results)
3. Mask colors in the range of defined threshold, and implement mask blur variable with Gaussian blur
4. Create copies of mask zone and add mask blur
5. Compile copies together

