# Fast Neural Style Transfer
A web app built using Django and PyTorch, which uses deep learning to apply the style of a selected artwork to the photo uploaded by the user.


<p align="center">
  <kbd>
  <img src="https://user-images.githubusercontent.com/55808644/83978611-70877b80-a926-11ea-812f-91594694c890.gif" width="750" align="center" />
  </kbd>
</p>

* The app uses the strategy proposed by **Johnson *et al*** in their paper, **Perceptual Losses for Real-Time Style Transfer and Super-Resolution**.
* This is an improvement from the traditional approach for style transfer which created a brand new image from the content and style image by optimizing a loss function on the spot, which was quite time consuming.
* The idea proposed by Johnson *et al* is to train a neural network to learn a style once and then apply style transfer on new images just by running them through the model.
* This reduces the time taken for styling the image from 20 seconds to just **20 - 50 milliseconds**.
* The models used for this app were trained on 25000 images from the COCO dataset.
* The app uses AJAX for sending the request to style the user's image and updating the webpage.
