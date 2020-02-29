## Interface

接口自动化测试脚本
```text
测试过程：
    1.向测试数据库插入测试数据（一般使用测试数据库，不对真实数据库造成污染）;
    2.调用被测系统接口；
    3.接口对数据进行处理，并返回结果；
    4.通过python中的unittest单元测试框架断言接口返回的数据，并生成测试报告。
```

AppiumPython  客户端自动化测试

selleniumPython web自动化测试

### 以下是测试工具资料

1. UFT（别名：QuickTest Professional简称QTP）是一种自动化测试工具，以VBScirpt为内嵌语言
2. Robotium是一款国外的Android自动化测试框架，主要针对Android平台的应用进行黑盒自动化测试，它提供了模拟各种手势操作（点击、长按、滑动等）、查找和断言机制的API，能够对各种控件进行操作。
3. TestNG是Java中的一个测试框架， 类似于JUnit 和NUnit, 功能都差不多， 只是功能更加强大，使用也更方便。

4. appium 是一个自动化测试开源工具，支持 iOS 平台和 Android 平台上的原生应用，web应用和混合应用

5. Selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。

6. mitmproxy 就是用于 MITM 的 proxy，MITM 即中间人攻击（Man-in-the-middle attack）。用于中间人攻击的代理首先会向正常的代理一样转发请求，保障服务端与客户端的通信，其次，会适时的查、记录其截获的数据，或篡改数据，引发服务端或客户端特定的行为。

7. HTMLTestRunner 为unittest单元测试框架的扩展，利用它所提供的HTMLTestRunner()类来替换unittest单元测试框架的TextTestRunner()类，从而生成HTML格式的测试报告。
8.Monkey是Android SDK提供的一个命令行工具，可以简单方便的发送伪随机的用户事件流，对Android APP做压力（稳定性）测试。主要是为了测试app是否存在无响应和崩溃的情况。




11. monkeyrunner工具同Monkey工具的差别:

- Monkey：
Monkey工具直接运行在设备或模拟器的adb shell中，生成用户或系统的伪随机事件流。
monkeyrunner：
monkeyrunner工具则是在工作站上通过API定义的特定命令和事件控制设备或模拟器。
 
- Monkeyrunner缺点：
1、monkeyrunner本身存在bug，长时间跑，自身也会出现crash
2、monkeyrunner无论导入什么库，都是app层的，黑盒测试，相当于android ui layout上又架了一层，模拟点击操作




