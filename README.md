# web-automation
# overview
Everyone wants to be as smart as machine and robots, so they create softwares which makes machine to do their such work.
whatsapp-automation is a such software which can easily operate the whatsapp web in your webbrowser and can do whatever you want like such writing a message and sending it to the perticular group or group of peoples, not only just sending message it can read any of the message for you, can send images, document files etc.

So now the question arrises why did I started this project, whats the main idea behind it, what are the problems I had faced and so and so....

# So why did I started this project?
  
  Everyone is well aware about how whatsapp work and how it has became a part of everyday life.....
 
 Have you ever think you can only type the message in a perticular chat only and you can send it over there only and if you have to send it to any other eiter you have to type it again of you will simply have to forward that message to other people and that thing will show forwarded message, over every message you forward from one person to another.
And if you have lots of different message which are written somewhere else you first have to open that message and then copy it and then go to the whatsapp and then send it, seriously it takes lots of time, or if have a something that you have to remind to that person and for that you have to message again and again to that person after a fixed interval of time, Then this software has solution to every such problem. 

I had encountered with some of these problem in my college when teachers have to send the same messages to different groups and they were like its very annoying thing to first type a huge message and then send it to different groups and it takes lots of time for searching perticular neme of the person and the group and then sending the message to them.

# what is the main idea behind it?

The idea was as simple as making a cup of tea....
To make a software which can solve each of the problem as memtioned above, to automate the whats app and the web browser in such a way the the user doesn't have to do much thing we just simply run this software in our pc and give out some of the entries to the required fields and just simply lay back and let the software to do each and every task.

# what are the problem I had faced?
There were some problems like which language to choose as this software will work for whatsapp web and whatsapp web is created using scripting languages and though css also for the designing part and firstly we have to automate the webpage like a way that whenever the software go to the running state it automatically opens the perticular web browser search whatsapp over there and open the whatsapp web page..... This was the first step. 

In the second step-
It should scan the QR Code for the linking of the whatsapp web with the mobile phone.
It can be achieved in two ways either you can do it manually everytime you run the software of let  the software to that task too.... And if the software had to do that thing then the problem is how to do that thing.

Now for the first two steps of the problem we used the python language as python language provides access to many of its inbuild libraries for which we dont have to write the code just simply import it and use it.

There's a library called webbrowser in the python which i came to know after searching the solution to this problem over different websites, this library just open the webbrowser and make you jump to the destination page.

But this library doesn't work as normal, it although opens the webbrowser but it will not make you jump to the destinated web browser at starting for that thing you additionally have to install the driver to that webbrowser which you are using for example if you are using chrome then you have download the chrome driver and you have to add the path of that downloaded driver to the software or to the source file.

Now after all these such things and solving the problem the next step was to search the name of the perticular person or the group and select that person chat and then type and send the message.

now to achieve that thing there are any of the python library but each library has a different way to work, some of them work directly and some of them just work for single person message only.

Have you guys heared about SELENIUM ??
It is a python library that allows you to automate any of the webpage either it is facebook or whatsapp or any of the other page which you want to automate it can do that thing also.

But the problem with this library is that its works through the XPath, means the webbrowser which we want to automate with this library we have to give the xpath of the textbox or the inputfiels or selection text to the source code.
But this library worth it each and every process it made me do...

There were some more problems which i had face but are not that major ones.

But seriously this library(python selenium) solved many of my major problems and my code finally worked and in the same way as expected but there are many changes to do...

# Libraries used
The following libraries were used:

<ul> 
  <li> selenium</li>
  <li>selenium webbrowser</li>
  <li>selenium webdriver
    <ul><li>selenium waits</li>
        <li>selenium keys</li> 
    </ul>
  </li>
</ul>
  
        
