# Simple Calculator Made With Tkinter

I haven't used any themes of colours with the UI, just created the calculator to practice basic tkinter functionality and python data types.
I have used an Entry widget as a field where you enter your numbers and a Label widget as a field to display what has been entered previously.

![Addition](https://user-images.githubusercontent.com/123562461/230423048-40fe5e89-f8a5-4ba9-8e3f-cdaaf5b51588.png)

The calculator itself is very simple, withhout any extra functionality, just basic types of operations are supported. At the moment I haven't created a function to take the float after a division and do an operation with it, and take the remainder out if it ends on .00 or diplay it otherwise. This will be left for the future.

When dividing by 0, you get an error message to the screen and need to clear the result and start over.

![Div By Zero](https://user-images.githubusercontent.com/123562461/230423597-2ce92f4e-78c3-4ea8-92da-caf18f08e785.png)

Otherwise it gives you a floating point number, but you cannot at the moment do a next operation with it.

![Div Result](https://user-images.githubusercontent.com/123562461/230424140-b0356a07-69db-4ff2-aae4-cc336c3075c8.png)

I have bind the number keys from 0-9 to typing in the entry widget and also the operants plus, minus, multiplicator, divisor and also the equal sign to generate the appropriate response. There is a bug where, if you click on the entry widget and start typing numbers they will be displayed twice. That is due to the event that you are now typing a string in the entry box, and there is no break point to see that this event has happened and unbind the buttons, or just don't execute the function on their pressing. This will be resolved eventually.

### Link to [demo file](https://github.com/Dan-Mihaylov/calculator/tree/main/output) .
