import random
from typing import Dict, List
import re

#前三条测试数据
dat = [{'urls': ['javascript:(function(){window.ALIPAYVIEWAPPEARED=1})();',
                 'http://www.baidu.com',
                 'javascript:(function(){window.ENABLEINPAGEINPUT=false;})()'],
        'path': 'com/alipay/mobile/nebulacore/web/H5ScriptLoader.java'},
{'urls': ['javascript:(function(){window.ALIPAYVIEWAPPEARED=1})();',
                 'javascript:(function(){window.ENABLEINPAGEINPUT=false;})()'],
        'path': 'com/alipay/mobile/nebulacore/web/H5ScriptLoader.java'},
    {'urls': ['https://api.weibo.cn/2/sdk/login13145652786', 'http://e18727829api.weibo.cn/2/sdk/login'],
        'path': 'test1.java'},
       {'urls': ['//api.weib18337162729o.com/2/proxy/sdk/statistic.json'],
        'path': 'test2.java'}, {
           'urls': ['http://www.baidu.com',
                    'https://service.weibo.com/share/mobilesdk_uppic.php89383898'],
           'path': 'test3.java'},
    {'urls': ['https://api.weibo.cn/2/sdk/login', 'http://api.weibo.cn/2/sdk/login'],
        'path': 'com/sina/weibo/sdk/network/intercept/GuestParamInterception.java'},
       {'urls': ['https://api.weibo.com/2/proxy/sdk/statistic.json'],
        'path': 'com/sina/weibo/sdk/statistic/LogReport.java'}, {
           'urls': ['https://service.weibo.com/share/mobilesdk.php',
                    'https://service.weibo.com/share/mobilesdk_uppic.php'],
           'path': 'com/sina/weibo/sdk/web/param/ShareWebViewRequestParam.java'},
       {'urls': ['https://open.weibo.cn/oauth2/authorize?'], 'path': 'com/sina/weibo/sdk/auth/BaseSsoHandler.java'},
       {'urls': ['https://api.weibo.com/oauth2/access_token'],
        'path': 'com/sina/weibo/sdk/auth/AccessTokenKeeper.java'},
       {'urls': ['https://paygate-yf.meituan.com/paygate/notify/alipay/paynotify/simple'],
        'path': 'com/alipay/test/a.java'},
       {'urls': ['data:image/png;base64,'], 'path': 'com/alipay/mobile/nebulax/integration/mpaas/view/a.java'}, {
           'urls': ['https://render.alipay.com/p/s/errorpage/?',
                    'https://render.alipay.com/p/s/h5misc/resource_error?url='],
           'path': 'com/alipay/mobile/nebulax/integration/mpaas/extensions/TinyAppUrlIntercepExtension.java'}, {
           'urls': ['https://render.alipay.com/p/w/websecurity/securityLink.html?url=', 'www.25pp.com/down',
                    'https://render.alipay.com/p/w/websecurity/redirectLink.html?url='],
           'path': 'com/alipay/mobile/nebulax/integration/mpaas/extensions/NebulaSchemaInterceptExtension.java'}, {
           'urls': ['https://render.alipay.com/p/w/websecurity/securityLink.html',
                    'https://render.alipay.com/p/w/websecurity/redirectLink.html'],
           'path': 'com/alipay/mobile/nebulax/integration/mpaas/proxy/impl/NebulaCommonAbilityProxy.java'},
       {'urls': ['https://render.alipay.com/p/s/tinyapperror?appId=%s&errorCode=%s'],
        'path': 'com/alipay/mobile/nebulax/resource/biz/DefaultResourceBizProxy.java'},
       {'urls': ['https://render.alipay.com/p/s/tinyapperror/?appId=%s&errorCode=%d'],
        'path': 'com/alipay/mobile/nebulax/resource/biz/MainPrepareController.java'},
       {'urls': ['https://mobilegw.alipay.com/mgw.htm'],
        'path': 'com/alipay/mobile/nebulax/resource/api/NXResourceNetworkProxy.java'},
       {'urls': ['https://appx-ng/'], 'path': 'com/alipay/mobile/nebulax/resource/a/b.java'},
       {'urls': ['https://appx', 'https://cube'],
        'path': 'com/alipay/mobile/nebulax/resource/extensions/ResourceInterceptExtension.java'}, {
           'urls': ['https://resource/', 'https://alipay.com/h5container/redirect_link.html',
                    'https://alipay.com/h5container/security_link.html', 'https://resource/nebula-addcors/',
                    'https://alipay.com/h5container/white_link.html',
                    'https://resource/nebula-addcors/Alibaba-PuHuiTi-Regular-GB2312.ttf',
                    'https://resource/nebula-addcors/Alibaba-PuHuiTi-Medium-GB2313.ttf'],
           'path': 'com/alipay/mobile/nebulax/resource/extensions/ResourceProviderExtension.java'},
       {'urls': ['https://appx/'], 'path': 'com/alipay/mobile/nebulax/engine/webview/v8/NXV8Worker.java'},
       {'urls': ['javascript:{window.__alipayConsole__'], 'path': 'com/alipay/mobile/nebulax/engine/webview/c/c.java'},
       {'urls': ['https://render.alipay.com/p/s/h5misc/resource_error?url='],
        'path': 'com/alipay/mobile/nebulax/engine/webview/c/d.java'},
       {'urls': ['https://render.alipay.com/p/s/h5misc/resource_error?url='],
        'path': 'com/alipay/mobile/nebulax/engine/webview/c/b.java'},
       {'urls': ['https://cube/native-jsfm.js'], 'path': 'com/alipay/mobile/nebulax/engine/cube/a.java'},
       {'urls': ['https://alipay.kylinBridge'], 'path': 'com/alipay/mobile/worker/H5WorkerControllerProvider.java'},
       {'urls': ['https://alipay.worker.com/worker', 'data:__workerjs});'],
        'path': 'com/alipay/mobile/worker/WebWorker.java'}, {
           'urls': ['javascript:window.worker', 'https://alipay.worker.com/create_worker',
                    "javascript:window.worker.postMessage('", 'javascript:window.worker.terminate();'],
           'path': 'com/alipay/mobile/worker/multiworker/MultiJsWorker.java'}, {'urls': ['https://alipay.kylinBridge'],
                                                                                'path': 'com/alipay/mobile/worker/remotedebug/RemoteDebugWorkerControllerProvider.java'},
       {'urls': ['https://appx'], 'path': 'com/alipay/mobile/worker/v8worker/Helpers.java'},
       {'urls': ['https://appx/worker.js'], 'path': 'com/alipay/mobile/worker/v8worker/JSWorker.java'},
       {'urls': ['https://appx/af-appx.worker.min.js', 'https://alipay.kylinBridge', 'https://appx/'],
        'path': 'com/alipay/mobile/worker/v8worker/ImportScriptsCallback.java'}, {
           'urls': ['https://appx/security-patch.min.js', 'https://appx/af-appx.worker.min.js',
                    'https://appx/v8.worker.js', 'https://appx/af-appx.worker.min.js,'],
           'path': 'com/alipay/mobile/worker/v8worker/V8Worker.java'},
       {'urls': ['https://render.alipay.com/p/s/h5misc/resource_error?url='],
        'path': 'com/alipay/mobile/nebulacore/Nebula.java'}, {'urls': ['javascript:{window.__alipayConsole__'],
                                                              'path': 'com/alipay/mobile/nebulacore/web/H5WebChromeClient.java'},
       {'urls': ['javascript:(function(){window.ALIPAYVIEWAPPEARED=1})();', 'javascript:if(typeof',
                 'javascript:(function(){window.disableNativeTextArea=true;})()',
                 'javascript:(function(){window.ENABLEINPAGEINPUT=true;})()',
                 'javascript:(function(){window.ENABLEINPAGEINPUT=false;})()'],
        'path': 'com/alipay/mobile/nebulacore/web/H5ScriptLoader.java'},
       {'urls': ['https://fucard'], 'path': 'com/alipay/mobile/nebulacore/web/H5WebViewClient.java'},
       {'urls': ['http://patriot.cs.pp.cn/api/resource.app.detect'],
        'path': 'com/alipay/mobile/nebulacore/util/H5PPQueryThread.java'},
       {'urls': ['https://hpmweb.alipay.com/vorlon', 'https://hpmweb.alipay.com/bugme/domScript'],
        'path': 'com/alipay/mobile/nebulacore/dev/provider/H5DevPlugin.java'},
       {'urls': ['https://www.alipay.com'], 'path': 'com/alipay/mobile/nebulacore/appcenter/center/H5AppCenter.java'}, {
           'urls': ['https://render.alipay.com/p/s/h5container/index', 'https://appx', 'https://appx/af-appx.min.js',
                    'https://appx/af-appx.worker.min.js', 'https://resource/alipaynumber-regular.ttf',
                    'https://resource/nebula-addcors/Alibaba-PuHuiTi-Regular-GB2312.ttf',
                    'https://resource/nebula-addcors/Alibaba-PuHuiTi-Medium-GB2313.ttf', 'https://appx/index.html',
                    'https://alipay.com/h5container/un_safe.html',
                    'https://a.alipayobjects.com/bridgeapi/1.0/jsready.js', 'https://bugme.cfg'],
           'path': 'com/alipay/mobile/nebulacore/core/H5ContentProviderImpl.java'},
       {'urls': ["javascript:location.replace('", 'javascript:(function(){window.ALIPAYVIEWAPPEARED=1})();'],
        'path': 'com/alipay/mobile/nebulacore/core/H5PageImpl.java'},
       {'urls': ["javascript:location.replace('"], 'path': 'com/alipay/mobile/nebulacore/ui/H5FragmentManager.java'}, {
           'urls': ['https://render.alipay.com/p/w/websecurity/securityLink.html',
                    'https://render.alipay.com/p/w/websecurity/redirectLink.html'],
           'path': 'com/alipay/mobile/nebulacore/plugin/H5ClipboardPlugin.java'}, {
           'urls': ['https://render.alipay.com/p/s/i/?scheme=',
                    'https://render.alipay.com/p/w/websecurity/securityLink.html',
                    'https://render.alipay.com/p/w/websecurity/redirectLink.html'],
           'path': 'com/alipay/mobile/nebulacore/plugin/H5PagePlugin.java'}, {'urls': ["javascript:location.replace('"],
                                                                              'path': 'com/alipay/mobile/nebulacore/plugin/H5NewJSAPIPermissionPlugin.java'},
       {'urls': ['javascript:var', 'javascript:componentsManager.renderV2('],
        'path': 'com/alipay/mobile/nebulacore/plugin/H5EmbedViewPlugin.java'}, {
           'urls': ['https://render.alipay.com/p/s/errorpage/?',
                    'https://render.alipay.com/p/s/h5misc/resource_error?url=',
                    'https://render.alipay.com/p/w/websecurity/securityLink.html?url=',
                    'https://alipay.com/h5container/un_safe.html', 'www.25pp.com/down',
                    'https://render.alipay.com/p/w/websecurity/redirectLink.html?url='],
           'path': 'com/alipay/mobile/nebulacore/plugin/H5UrlInterceptPlugin.java'},
       {'urls': ['https://render.alipay.com/p/w/websecurity/securityLink.html?url='],
        'path': 'com/alipay/mobile/nebulacore/plugin/H5ApkLoadPlugin.java'},
       {'urls': ['javascript:(function(){if(typeof'], 'path': 'com/alipay/mobile/nebulacore/bridge/H5BridgeImpl.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#indent-output'],
        'path': 'com/alipay/mobile/quinox/utils/sp/XmlUtils.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#indent-output'],
        'path': 'com/alipay/mobile/quinox/utils/sp/FastXmlSerializer.java'},
       {'urls': ['http://schemas.android.com/apk/res/android'],
        'path': 'com/alipay/mobile/antui/basic/AUTextView.java'}, {
           'urls': ['https://mdap.alipay.com/loggw/eggExtLog.do', 'http://mdap.alipaylog.com/loggw/extLog.do',
                    'https://mdap.alipay.com/loggw/report_egg_diangosis_upload_status.htm',
                    'http://mdap.alipaylog.com/loggw/report_diangosis_upload_status.htm'],
           'path': 'com/alipay/mobile/logmonitor/util/upload/UploadConstants.java'},
       {'urls': ['http://www.donotshow.me/instead'],
        'path': 'com/alipay/mobile/logmonitor/analysis/TrafficPowerHandler.java'},
       {'urls': ['http://c3x.me/', 'http://ofo.so/'],
        'path': 'com/alipay/mobile/liteprocess/ScanResultSubscriber.java'}, {
           'urls': ['http://cn-hangzhou-mas-log.cloud.alipay.com/loggw/logUpload.do',
                    'http://mdap-1-64.test.alipay.net', 'https://cn-hangzhou-mgs-gw.cloud.alipay.com/mgw.htm',
                    'http://mobilegw.aaa.alipay.net/mgw.htm', 'https://mobilegw.alipay.com/mgw.htm',
                    'https://mobilegwpre.alipay.com/mgw.htm', 'http://mobilegw.test.alipay.net/mgw.htm',
                    'http://mdap.alipaylog.com', 'http://openapi.stable.alipay.net/gateway.do',
                    'https://openapi.alipay.com/gateway.do',
                    'http://139.224.94.200/gateway/identification/simulate/face/initialize',
                    'https://openapi.prefromoffice.alipay.net/gateway.do',
                    'http://139.224.138.243/gateway/identification/simulate/face/initialize',
                    'http://openapi-1-64.test.alipay.net/gateway.do'],
           'path': 'com/alipay/mobile/security/bio/workspace/Env.java'},
       {'urls': ['https://render.alipay.com/p/f/fd-j8l9yjja/index.html'],
        'path': 'com/alipay/mobile/security/bio/config/bean/NavigatePage.java'},
       {'urls': ['http://apache.org/xml/features/disallow-doctype-decl'],
        'path': 'com/alipay/mobile/framework/util/xml/MetaInfoXmlParser.java'},
       {'urls': ['https://www.alipay.com/webviewbridge'],
        'path': 'com/alipay/mobile/securitycommon/taobaobind/util/AUH5Plugin.java'},
       {'urls': ['https://www.alipay.com/webviewbridge'],
        'path': 'com/alipay/mobile/securitycommon/taobaobind/util/H5Wrapper.java'},
       {'urls': ['https://www.alipay.com/webviewbridge'],
        'path': 'com/alipay/mobile/securitycommon/taobaobind/util/TaobaoBindUtil.java'},
       {'urls': ['http://www.taobao.com'], 'path': 'com/alipay/mobile/securitycommon/aliauth/AliAuthConstants.java'},
       {'urls': ['https://www.alipay.com/'],
        'path': 'com/alipay/mobile/nebulaappproxy/ipc/H5EventHandlerServiceImpl.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/nebulaappproxy/api/H5AppProxyUtil.java'}, {
           'urls': ['https://a.alipayobjects.com/u/h5/js/201507/5I3Q4qyENx.js',
                    'https://a.alipayobjects.com/u/h5/js/201506/5F34WsaYn7.js',
                    'https://t.alipayobjects.com/images/rmsweb/T1WrJgXfXdXXXXXXXX.js',
                    'https://t.alipayobjects.com/images/rmsweb/T1WApgXi0bXXXXXXXX.js',
                    'https://wappaygw.alipay.com/home/exterfaceAssign.htm',
                    'https://mclient.alipay.com/home/exterfaceAssign.htm',
                    'https://maliprod.alipay.com/batch_payment.do', 'https://mali.alipay.com/batch_payment.do',
                    'https://maliprod.alipay.com/w/trade_pay.do', 'https://mali.alipay.com/w/trade_pay.do',
                    'https://wappaygw.alipay.com/service/rest.htm', 'https://110.75.143.65/service/rest.htm',
                    'https://110.75.147.65/service/rest.htm', 'file:///',
                    'http://patriot.cs.pp.cn/api/resource.app.detect',
                    'https://gw.alicdn.com/bao/uploaded/LB1KgvQQpXXXXauXVXXXXXXXXXX.zip', 'https://d.alipay.com/?',
                    'https://ds.alipay.com/?', 'https://render.alipay.com/p/s/i?', 'https://render.alipay.com/p/s/i/?',
                    'https://render.alipay.com/p/s/i/index?'],
           'path': 'com/alipay/mobile/nebulaappproxy/api/config/WalletDefaultConfig.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/nebulaappproxy/utils/TinyappUtils.java'},
       {'urls': ['https://render.alipay.com/p/s/h5misc/resource_error?url='],
        'path': 'com/alipay/mobile/nebulaappproxy/plugin/tinyapp/TinyTlsWhiteListPlugin.java'},
       {'urls': ['https://resource/'],
        'path': 'com/alipay/mobile/nebulaappproxy/plugin/tinyapp/H5ShareImageUrlPlugin.java'},
       {'urls': ['https://render.alipay.com/p/s/updatex'],
        'path': 'com/alipay/mobile/nebulaappproxy/plugin/tinyapp/TinyAppAlipayUpdataPlugin.java'},
       {'urls': ['https://h5.m.taobao.com/'],
        'path': 'com/alipay/mobile/nebulaappproxy/plugin/tinyapp/TinyAppMTopPlugin.java'}, {
           'urls': ['https://2015042700050887.hybrid.alipay-eco.com', 'https://2017021305648824.hybrid.alipay-eco.com',
                    'https://2015121700992100.hybrid.alipay-eco.com'],
           'path': 'com/alipay/mobile/nebulaappproxy/plugin/auth/H5OpenAuthPlugin.java'},
       {'urls': ['javascript:(function(){function'],
        'path': 'com/alipay/mobile/nebulaappproxy/tinymenu/TinyMenuPopupWindow.java'},
       {'urls': ['javascript:(function(){function'],
        'path': 'com/alipay/mobile/nebulaappproxy/tinymenu/TinyBlurMenu.java'},
       {'urls': ["https://ds.alipay.com/?scheme='", 'file://xxxx'],
        'path': 'com/alipay/mobile/nebulaappproxy/tinymenu/TinyMenuUtils.java'}, {
           'urls': ['javascript:(function(){function',
                    'https://render.alipay.com/p/s/h5data/prod/popMenu/config/popmenu-h5data.json'],
           'path': 'com/alipay/mobile/nebulaappproxy/tinymenu/TinyActionSheetMenu.java'},
       {'urls': ['javascript:(function(){function'],
        'path': 'com/alipay/mobile/nebulaappproxy/tinymenu/corner/CornerMarkingData.java'}, {
           'urls': ['https://mdap.alipay.com/loggw/tinyapp/queryConfig.do',
                    'https://mdap.alipay.com/loggw/tinyapp/testLogUpload.do'],
           'path': 'com/alipay/mobile/nebulaappproxy/logging/TinyLoggingConfigManager.java'},
       {'urls': ['https://render.alipay.com/p/s/h5misc/resource_error'],
        'path': 'com/alipay/mobile/nebulaappproxy/superapi/mobilegw/model/MiniappCheckResultPB.java'},
       {'urls': ['data:image/png;base64,'], 'path': 'com/alipay/mobile/nebulabiz/provider/H5ErrorPageViewImpl.java'},
       {'urls': ['https://usr'], 'path': 'com/alipay/mobile/beehive/audio/plugin/AudioBackgroundPlayPlugin.java'},
       {'urls': ['https://usr'], 'path': 'com/alipay/mobile/beehive/audio/plugin/AudioForegroundPlayPlugin.java'},
       {'urls': ['http://wap.amap.com/'], 'path': 'com/alipay/mobile/beehive/util/MapUtil.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/beehive/util/TinyappUtils.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/beehive/plugin/SaveImageToAlbum.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/beehive/plugin/H5SaveVideoPlugin.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/beehive/plugin/H5ImageInfoPlugin.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/beehive/plugin/H5CompressImagePlugin.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/beehive/plugins/Constant.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/beehive/plugins/utils/PathToLocalUtil.java'},
       {'urls': ['https://gw.alipayobjects.com/os/nebulamng/AP_63300038-sign/80gf3b0kaa2.amr'],
        'path': 'com/alipay/mobile/nebula/util/H5PresetResUtil.java'}, {
           'urls': ['data:image/gif;base64,', 'data:image/x-icon;base64,', 'data:image/jpeg;base64,',
                    'data:image/png;base64,'], 'path': 'com/alipay/mobile/nebula/util/H5ImageUtil.java'},
       {'urls': ['file:///'], 'path': 'com/alipay/mobile/nebula/util/H5UrlHelper.java'},
       {'urls': ['javascript:(function(){if(typeof'], 'path': 'com/alipay/mobile/nebula/util/TestDataUtils.java'},
       {'urls': ['https://mobilegw.alipay.com/mgw.htm', 'https://mobilegwpre.alipay.com/mgw.htm'],
        'path': 'com/alipay/mobile/nebula/util/H5NetworkUtil.java'},
       {'urls': ['https://resource/', 'https://hpmweb.alipay.com/bugme/assets/mockScript'],
        'path': 'com/alipay/mobile/nebula/util/H5Utils.java'},
       {'urls': ['https://hpmweb.alipay.com/report/android/batch', 'https://hpmweb.alipay.com/report/android'],
        'path': 'com/alipay/mobile/nebula/dev/H5DevConfig.java'}, {
           'urls': ['https://a.alipayobjects.com/bridgeapi/1.0/jsready.js',
                    'https://alipay.com/h5container/h5_page_error.html',
                    'https://alipay.com/h5container/redirect_link.html',
                    'https://alipay.com/h5container/security_link.html', 'https://alipay.com/h5container/un_safe.html',
                    'https://alipay.com/h5container/white_link.html'],
           'path': 'com/alipay/mobile/nebula/appcenter/api/H5ContentProvider.java'},
       {'urls': ['https://render.alipay.com/p/s/tinyapperror/?appId=%s&errorCode=%d'],
        'path': 'com/alipay/mobile/nebula/appcenter/apphandler/H5AppHandler.java'}, {
           'urls': ['http://wapcenter.stable.alipay.net/api/app', 'https://nebula.alipay.com/api/app',
                    'https://nebula.pre.alipay.com/api/app', 'http://wapcenter.test.alipay.net/api/app'],
           'path': 'com/alipay/mobile/nebula/appcenter/openapi/H5AppOpenApiUrl.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/nebula/resourcehandler/H5ResourceHandlerUtil.java'},
       {'urls': ['http://xml.apache.org/xslt}indent-amount'], 'path': 'com/alipay/mobile/android/verify/logger/a.java'},
       {'urls': ['javascript:(function(){if(typeof'], 'path': 'com/alipay/mobile/android/verify/bridge/b/a.java'},
       {'urls': ['javascript:(function(){if(typeof'], 'path': 'com/alipay/mobile/android/verify/bridge/b/b.java'},
       {'urls': ['http://amdc.alipay.com/query'],
        'path': 'com/alipay/mobile/common/transport/utils/ReadSettingServerUrl.java'},
       {'urls': ['https://promotion.alipay.com/mgw.htm'],
        'path': 'com/alipay/mobile/common/transport/config/TransportConfigureItem.java'}, {
           'urls': ['https://mclient.alipay.com/gateway.do', 'http://amdc.alipay.com/query',
                    'https://d.alipay.com/mbresultyy/public.htm', 'https://ccdcapi.alipay.com/cacheWapCardInfo.json',
                    'http://mdap.alipay.com/loggw/log.do', 'https://d.alipay.com',
                    'https://d.alipay.com/mbresultyy/prc.htm', 'http://d.alipay.net/cpbSign/nonsupport.htm',
                    'https://d.alipay.com/cpbSign/nonsupport.htm', 'http://d.alipay.net/cpbSign/add.htm',
                    'https://d.alipay.com/cpbSign/add.htm',
                    'https://cschannel.alipay.com/mobile/csrouter.htm?platform=android',
                    'https://clientsc.alipay.com/account/gateway.htm',
                    'https://wapcashier.alipay.com/home/resetPayPwd.htm?src=alipayclient&awid=',
                    'https://wappaygw.alipay.com/service/rest.htm', 'http://maliprod.alipay.com/w/trade_pay.do',
                    'http://mali.alipay.com/w/trade_pay.do', 'http://maliprod.alipay.com/batch_payment.do',
                    'http://mali.alipay.com/batch_payment.do'],
           'path': 'com/alipay/mobile/common/helper/ReadSettingServerUrl.java'}, {'urls': ['www.taobao.com'],
                                                                                  'path': 'com/alipay/mobile/common/transportext/biz/diagnose/network/NetworkCheck.java'},
       {'urls': ['www.taobao.com'],
        'path': 'com/alipay/mobile/common/transportext/biz/diagnose/network/NetworkDiagnose.java'},
       {'urls': ['www.taobao.com'],
        'path': 'com/alipay/mobile/common/transportext/biz/diagnose/network/NetworkDiagnoseUtil.java'},
       {'urls': ['www.taobao.com'],
        'path': 'com/alipay/mobile/common/transportext/biz/diagnose/network/Traceroute.java'},
       {'urls': ['http://mdap-1-64.test.alipay.net'], 'path': 'com/alipay/mobile/common/logging/LogContextImpl.java'}, {
           'urls': ['https://mdap.alipay.com', 'https://loggw.alipay.com', 'https://loggw-extiny.alipay.com',
                    'http://mdap.alipaylog.com'], 'path': 'com/alipay/mobile/common/logging/api/LogContext.java'},
       {'urls': ['https://gw.alipayobjects.com/config'],
        'path': 'com/alipay/mobile/common/logging/strategy/LogStrategyManager.java'},
       {'urls': ['http://mugw.alipay.com:443', 'http://mdgw.alipay.com:443'],
        'path': 'com/alipay/mobile/common/nbnet/biz/util/URLConfigUtil.java'},
       {'urls': ['https://usr/', 'https://usr'], 'path': 'com/alipay/mobile/aompfilemanager/ConversionPathTool.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/aompfilemanager/a.java'},
       {'urls': ['https://resource/', 'https://usr/'],
        'path': 'com/alipay/mobile/aompfilemanager/h5plugin/H5FilePlugin.java'},
       {'urls': ['https://mdgw.alipay.com/rest/1.0/file?fileid='],
        'path': 'com/alipay/mobile/aompfilemanager/h5plugin/H5UploadPlugin.java'},
       {'urls': ['https://usr/', 'https://usr', 'https://resource/'],
        'path': 'com/alipay/mobile/aompfilemanager/h5plugin/H5FSManagePlugin.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/aompfilemanager/utils/io/TinyAppFileUtils.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/mobile/aompfilemanager/a/c.java'},
       {'urls': ['https://appx/af-appx.min.js'], 'path': 'com/alipay/mobile/nebulauc/impl/UCWebView.java'},
       {'urls': ['https://appx/af-appx.min.js'], 'path': 'com/alipay/mobile/nebulauc/impl/JsPreloadWebviewClient.java'},
       {'urls': ['https://appx/'], 'path': 'com/alipay/mobile/nebulauc/impl/network/AlipayRequest.java'},
       {'urls': ['https://alipay.kylinBridge'],
        'path': 'com/alipay/mobile/nebulauc/impl/serviceworker/H5ServiceWorkerControllerProviderImpl.java'},
       {'urls': ['https://alipay.kylinBridge'],
        'path': 'com/alipay/mobile/nebulauc/impl/serviceworker/H5ServiceWorkerClient.java'},
       {'urls': ['https://www.alipay.com'],
        'path': 'com/alipay/mobile/nebulauc/impl/serviceworker/H5ServiceWorkerPageManager.java'},
       {'urls': ['https://gw.alipayobjects.com/os/basement_prod/bcefd687-d09c-40fc-8298-7e6e106336a7.zip'],
        'path': 'com/alipay/mobile/nebulauc/impl/setup/UcVideoSetup.java'},
       {'urls': ['javascript:document.activeElement'],
        'path': 'com/alipay/mobile/nebulauc/input/H5NumInputKeyboardM57.java'}, {
           'urls': ['http://custweb.alipay.net/register/h5/quick/index?goto=%s&scene=MINIMAL_REGISTRATION&mobile=%s',
                    'https://custweb.alipay.com/register/h5/quick/index?goto=%s&scene=MINIMAL_REGISTRATION&mobile=%s',
                    'https://custweb.test.alipay.net/register/h5/quick/index?goto=%s&scene=MINIMAL_REGISTRATION&mobile=%s'],
           'path': 'com/alipay/mobile/accountopenauth/common/OAuthConstant.java'},
       {'urls': ['https://mcgw.alipay.com/sdklog.do'], 'path': 'com/alipay/sdk/packet/impl/d.java'}, {
           'urls': ['https://mobilegw.alipay.com/mgw.htm', 'https://mobilegw.alipaydev.com/mgw.htm',
                    'http://m.alipay.com/?action=h5quit', 'https://wappaygw.alipay.com/home/exterfaceAssign.htm?',
                    'https://mclient.alipay.com/home/exterfaceAssign.htm?'], 'path': 'com/alipay/sdk/cons/a.java'},
       {'urls': ['http://h5.m.taobao.com/trade/paySuccess.html?bizOrderId=$OrderId$&'],
        'path': 'com/alipay/sdk/data/a.java'}, {'urls': ['https://ds.alipay.com/fd-inhm9zcq/index.html',
                                                         'https://render.alipay.com/p/f/fd-jldmt3yw/index.html',
                                                         'https://render.alipay.com/p/f/fd-iztnkm19/index.html',
                                                         'https://ds.alipay.com/help/icon.htm',
                                                         'https://tms.alicdn.com/go/chn/member/agreement.php'],
                                                'path': 'com/alipay/user/mobile/AliuserConstants.java'},
       {'urls': ['https://www.alipay.com/webviewbridge'],
        'path': 'com/alipay/user/mobile/loginbiz/BaseLoginService.java'}, {
           'urls': ['https://mobilegw.alipay.com/mgw.htm', 'http://mobilegw.stable.alipay.net/mgw.htm',
                    'http://mobilegw-1-64.test.alipay.net/mgw.htm', 'http://mobilegw.aaa.alipay.net/mgw.htm'],
           'path': 'com/alipay/deviceid/module/x/b.java'}, {
           'urls': ['https://gw.alicdn.com/tfs/TB1.32hrFuWBuNjSspnXXX1NVXa-84-84.png',
                    'https://gw.alicdn.com/tfs/TB1njS2rFOWBuNjy0FiXXXFxVXa-84-84.png',
                    'https://img.alicdn.com/tfs/TB1QmsWA_tYBeNjy1XdXXXXyVXa-81-81.png',
                    'https://gw.alicdn.com/tfs/TB1uGvprL5TBuNjSspmXXaDRVXa-84-84.png',
                    'https://gw.alicdn.com/tfs/TB1tDzLrNGYBuNjy0FnXXX5lpXa-84-84.png',
                    'https://gw.alicdn.com/tfs/TB1j7Vfr_tYBeNjy1XdXXXXyVXa-84-84.png',
                    'https://gw.alicdn.com/tfs/TB1iveUrHGYBuNjy0FoXXciBFXa-84-84.png',
                    'https://gw.alicdn.com/tfs/TB1mZ05jvuSBuNkHFqDXXXfhVXa-84-84.png'],
           'path': 'com/alipay/android/phone/inside/main/action/utils/AFuncListProvider.java'},
       {'urls': ['https://inside-gateway.alipay.com/mgw.htm'],
        'path': 'com/alipay/android/phone/inside/openext/common/CommonUtils.java'},
       {'urls': ['https://mdap.alipay.com/loggw/sdkLogUpload.do'],
        'path': 'com/alipay/android/phone/inside/log/LogUploader.java'},
       {'urls': ['https://inside-gateway.alipay.com/mgw.htm'],
        'path': 'com/alipay/android/phone/inside/config/plugin/service/DynamicConfigLoadService.java'},
       {'urls': ['data:text/html;charset=utf-8;base64,'],
        'path': 'com/alipay/android/phone/inside/offlinecode/engine/webkit/WebkitJSEngine.java'},
       {'urls': ['https://cn-hangzhou-mgs-gw.cloud.alipay.com/mgw.htm', 'http://116.62.88.165/mgw.htm'],
        'path': 'com/alipay/android/phone/mobilecommon/rpc/AlipayRpcService.java'}, {'urls': ['file:///'],
                                                                                     'path': 'com/alipay/android/phone/mobilecommon/multimediabiz/biz/material/MaterialManager.java'},
       {'urls': ['file:///'], 'path': 'com/alipay/android/phone/mobilecommon/multimediabiz/biz/utils/PathUtils.java'},
       {'urls': ['http://%1$s/%2$s'],
        'path': 'com/alipay/android/phone/mobilecommon/multimediabiz/biz/client/util/DjangoConstant.java'},
       {'urls': ['http://%1$s/%2$s'],
        'path': 'com/alipay/android/phone/mobilecommon/multimediabiz/biz/client/api/infos/BaseApiInfo.java'},
       {'urls': ['http://127.0.0.1:'], 'path': 'com/alipay/multimedia/network/LocalNetworkProxy.java'},
       {'urls': ['https://resource/'], 'path': 'com/alipay/multimedia/js/base/MMH5SimplePlugin.java'},
       {'urls': ["javascript:setUserName('"], 'path': 'com/alipay/zoloz/toyger/workspace/NavWebViewClient.java'},
       {'urls': ['https://entphz.alipay.com/postToken.json', 'https://entpsz.alipay.com/postToken.json'],
        'path': 'com/alipay/apmobilesecuritysdk/proxydetect/EntpClient.java'},
       {'urls': ['http://%1$s/%2$s'], 'path': 'com/alipay/xmedia/apmutils/utils/DjangoConstant.java'},
       {'urls': ['https://api.xmpush.xiaomi.com/upload/crash_log?file='], 'path': 'com/xiaomi/mipush/sdk/w.java'}, {
           'urls': ['https://api.xmpush.xiaomi.com/upload/xmsf_log?file=',
                    'https://api.xmpush.xiaomi.com/upload/app_log?file='], 'path': 'com/xiaomi/mipush/sdk/u.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#process-namespaces'], 'path': 'com/xiaomi/push/gq.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#process-namespaces'], 'path': 'com/xiaomi/push/fo.java'},
       {'urls': ['http://%1$s/gslb/?ver=4.0'], 'path': 'com/xiaomi/push/cz.java'},
       {'urls': ['http://new.api.ad.xiaomi.com/logNotificationAdActions'], 'path': 'com/xiaomi/push/cq.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#process-namespaces'], 'path': 'com/xiaomi/push/fy.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#process-namespaces'], 'path': 'com/xiaomi/push/gr.java'},
       {'urls': ['http://www.jivesoftware.com/xmlns/xmpp/properties'], 'path': 'com/xiaomi/push/gj.java'},
       {'urls': ['www.baidu.com:80'], 'path': 'com/xiaomi/push/service/ae.java'},
       {'urls': ['http://resolver.msg.xiaomi.net/psc/?t=a'], 'path': 'com/xiaomi/push/service/bf.java'}, {
           'urls': ['https://cn.register.xmpush.xiaomi.com', 'https://register.xmpush.global.xiaomi.com',
                    'https://fr.register.xmpush.global.xiaomi.com', 'https://ru.register.xmpush.global.xiaomi.com',
                    'https://idmb.register.xmpush.global.xiaomi.com'], 'path': 'com/xiaomi/push/service/l.java'},
       {'urls': ['https://a.vmall.com/app/'], 'path': 'com/huawei/hms/update/e/l.java'},
       {'urls': ['https://play.google.com/store'], 'path': 'com/huawei/hms/update/c/a.java'},
       {'urls': ['https://metrics1.data.hicloud.com:6447', 'https://)'],
        'path': 'com/huawei/hms/api/HuaweiApiClient.java'},
       {'urls': ['https://play.google.com/store/apps/details?id=', 'https://a.vmall.com/'],
        'path': 'com/huawei/hms/support/api/push/a/a/a.java'},
       {'urls': ['http://b.qchannel03.cn/n/qtbs/v1'], 'path': 'com/sijla/b/a.java'},
       {'urls': ['https://truth.qchannel03.cn/truth', 'http://b.qchannel03.cn/n/qts'], 'path': 'com/sijla/f/a.java'},
       {'urls': ['http://b.qchannel03.cn/n/ard'], 'path': 'com/sijla/e/d.java'},
       {'urls': ['http://log.qchannel03.cn/n/dpz/'], 'path': 'com/sijla/c/a.java'},
       {'urls': ['javascript:TBAppLinkJsBridge.'], 'path': 'com/taobao/applink/util/a.java'},
       {'urls': ['https://)?((?:'], 'path': 'com/taobao/applink/util/e.java'}, {'urls': ['https://wgo.mmstat.com/%s',
                                                                                         'https://nbsdk-baichuan.alicdn.com/2.0.0/applink.htm?plat=android&appKey=%s',
                                                                                         'http://100.69.205.47/100.0.0/applink.htm?plat=android&appKey=%s',
                                                                                         'http://huodong.m.taobao.com/go/2085.html',
                                                                                         'http://oauth.m.taobao.com/authorize?response_type=code&client_id=%s&redirect_uri=%s&view=wap',
                                                                                         'http://h5.m.taobao.com/awp/core/detail.htm?id=%s&',
                                                                                         'http://shop.m.taobao.com/shop/shopIndex.htm?shop_id=%s&'],
                                                                                'path': 'com/taobao/applink/util/TBAppLinkUtil.java'},
       {'urls': ['javascript:TBAppLinkJsBridge._handleMessageFromNative(',
                 'javascript:TBAppLinkJsBridge._fetchQueue();'], 'path': 'com/taobao/applink/f/b.java'},
       {'urls': ['https://wgo.mmstat.com%s?'], 'path': 'com/taobao/applink/h/a.java'},
       {'urls': ['https://wgo.mmstat.com/ire.2.1'], 'path': 'com/taobao/applink/h/d.java'}, {
           'urls': ['http://100.69.165.28/agoo/report', 'http://agoodm.m.taobao.com/agoo/report',
                    'http://agoodm.wapa.taobao.com/agoo/report', 'http://100.69.168.33/agoo/report'],
           'path': 'com/taobao/accs/eudemon/EudemonManager.java'},
       {'urls': ['http://muvp.alibaba-inc.com/online/UploadRecords.do'],
        'path': 'com/ut/mini/internal/RealtimeDebugSwitch.java'}, {
           'urls': ['https://wap.cmpassport.com/resources/html/contract.html',
                    'https://e.189.cn/sdk/agreement/detail.do?appKey=E_189&hidetop=true&returnUrl=',
                    'https://opencloud.wostore.cn/authz/resource/html/disclaimer.html?fromsdk=true'],
           'path': 'com/mobile/auth/gatewayauth/Constant.java'}, {
           'urls': ['https://accountlink.taobao.com/confirmUnbind.htm', 'http://err.taobao.com/error2.html',
                    'https://aq.taobao.com/durex/wirelessValidate'],
           'path': 'com/ali/auth/third/accountlink/ui/a.java'}, {
           'urls': ['http://hz.pre.tbusergw.taobao.net/gw.do', 'http://hz.tbusergw.taobao.net/gw.do',
                    'https://mgw.m.taobao.com/gw.do'], 'path': 'com/ali/auth/third/core/rpc/a.java'}, {
           'urls': ['http://login.taobao.com/minisdk/login.htm',
                    'http://login.m.taobao.com/cooperation/bindLogin.htm?code=%s&IBB=%s&appkey=%s',
                    'https://accountlink.taobao.com/sdkUnbind.htm',
                    'http://login.waptest.tbsandbox.com/minisdk/login.htm',
                    'http://login.waptest.taobao.com/minisdk/login.htm',
                    'http://login.wapa.taobao.com/minisdk/login.htm', 'http://login.m.taobao.com/minisdk/login.htm',
                    'http://login.waptest.tbsandbox.com/cooperation/bindLogin.htm?code=%s&IBB=%s&appkey=%s',
                    'http://login.waptest.taobao.com/cooperation/bindLogin.htm?code=%s&IBB=%s&appkey=%s',
                    'http://login.wapa.taobao.com/cooperation/bindLogin.htm?code=%s&IBB=%s&appkey=%s',
                    'https://accountlink.daily.taobao.net/sdkUnbind.htm'],
           'path': 'com/ali/auth/third/core/config/ConfigManager.java'},
       {'urls': ['https://www.alipay.com/webviewbridge'], 'path': 'com/ali/auth/third/ui/LoginWebViewActivity.java'}, {
           'urls': ["javascript:window.HavanaBridge.onFailure(%s,'');",
                    "javascript:window.HavanaBridge.onFailure(%s,'%s');"],
           'path': 'com/ali/auth/third/ui/context/c.java'},
       {'urls': ['javascript:window.HavanaBridge.onSuccess(%s);', "javascript:window.HavanaBridge.onSuccess(%s,'%s');"],
        'path': 'com/ali/auth/third/ui/context/b.java'}, {
           'urls': ['https://log1.cmpassport.com:9443/log/logReport', 'https://onekey1.cmpassport.com/unisdk',
                    'http://www.cmpassport.com/unisdk'], 'path': 'com/cmic/sso/sdk/d/s.java'},
       {'urls': ['http://www.cmpassport.com/unisdk'], 'path': 'com/cmic/sso/sdk/b/a.java'},
       {'urls': ['https://config.cmpassport.com/client/uniConfig'], 'path': 'com/cmic/sso/sdk/b/a/a.java'},
       {'urls': ['https://config.cmpassport.com/client/uniConfig'], 'path': 'com/cmic/sso/sdk/b/c/a.java'},
       {'urls': ['http://wap.amap.com?type=aie'],
        'path': 'com/amap/bundle/dumpcrash/installerror/InstallErrorActivity.java'}, {
           'urls': ['http://h5.edaijia.cn/amap/', 'http://admin.1jiajie.com/gaode/index.php?online=1',
                    'http://passport.amap.com/sina/callback.php'],
           'path': 'com/amap/bundle/blutils/app/ConfigerHelper.java'}, {
           'urls': ['file:///android_asset/connect_error.html', 'file:///android_asset/not_found_error.html',
                    'javascript:(function', 'http://detail.tmall.com/item',
                    'https://h5.m.taobao.com/trip/train-amap/train-detail/index.html'],
           'path': 'com/amap/bundle/webview/page/WebViewPage.java'},
       {'urls': ['file:///android_asset/not_found_error.html', 'file:///android_asset/connect_error.html'],
        'path': 'com/amap/bundle/webview/widget/NormalWebView.java'}, {
           'urls': ['http://h5.m.taobao.com/mlapp/olist.html?ttid=@aligaode',
                    'file:///android_asset/not_found_error.html', 'file:///android_asset/connect_error.html',
                    'javascript:activeEvent('], 'path': 'com/amap/bundle/webview/widget/ExtendedWebView.java'}, {
           'urls': ['file:///android_asset/not_found_error.html', 'file:///android_asset/connect_error.html',
                    'file:///data/data/com.autonavi.minimap/'],
           'path': 'com/amap/bundle/webview/widget/AbstractBaseWebView.java'},
       {'urls': ['javascript:(function'], 'path': 'com/amap/bundle/webview/widget/WebViewEx.java'}, {
           'urls': ['file:///android_asset/not_found_error.html', 'file:///android_asset/connect_error.html',
                    'https://wap.amap.com/member/index.html#!/', 'https://h5.mobike.com',
                    'file:///data/data/com.autonavi.minimap/', 'javascript:activeEvent('],
           'path': 'com/amap/bundle/webview/widget/AmapWebView.java'},
       {'urls': ['http://muvp.alibaba-inc.com/online/UploadRecords.do'],
        'path': 'com/amap/bundle/behaviortracker/GDBehaviorTrackerImpl.java'},
       {'urls': ['https://m.alipay.com/VCDZA5R'],
        'path': 'com/amap/bundle/drive/ajx/module/ModuleCommonBusinessImpl.java'}, {
           'urls': ['http://aps.testing.amap.com/LoadOfflineData/repeatData',
                    'https://offline.aps.amap.com/LoadOfflineData/repeatData?',
                    'http://offline.aps.amap.com/LoadOfflineData/repeatData?'],
           'path': 'com/amap/location/offline/b/c/b.java'}, {
           'urls': ['http://aps.testing.amap.com/collection/collectData?src=baseCol&ver=v74',
                    'http://aps.testing.amap.com/collection/collectData?src=extCol&ver=v74'],
           'path': 'com/amap/location/b/e/c.java'}, {
           'urls': ['http://gnss-eph.oss-cn-hangzhou.aliyuncs.com/gnss-fence/fence.txt',
                    'http://gnss-eph.oss-cn-hangzhou.aliyuncs.com/ephemeris-hourly/latest.txt',
                    'http://gnss-eph.oss-cn-hangzhou.aliyuncs.com/ephemeris-hourly/',
                    'http://gnss-eph.oss-cn-hangzhou.aliyuncs.com/gnss-model/v1/'],
           'path': 'com/amap/location/sdk/e/h.java'}, {
           'urls': ['http://wb.testing.amap.com', 'http://group.myamap.com/', 'http://m.map.so.com',
                    'http://114.247.50.32', 'http://180.96.64.225/mo'], 'path': 'com/amap/location/sdk/a/f.java'},
       {'urls': ['https://awaken.amap.com/ws/awaken/open?'], 'path': 'com/amap/location/sdk/a/b.java'}, {
           'urls': ['http://maps.testing.amap.com/ws/transfer/auth/aps/locate',
                    'http://aps.testing.amap.com/APS/r?&q=0&ver=', 'http://aps.oversea.amap.com/APS/r?&q=0&ver='],
           'path': 'com/amap/location/protocol/b/a.java'}, {
           'urls': ['http://xml.org/sax/features/external-general-entities',
                    'http://xml.org/sax/features/external-parameter-entities'],
           'path': 'com/amap/location/protocol/e/f.java'}, {
           'urls': ['http://aps.testing.amap.com/conf/r?type=3&mid=300&sver=140',
                    'https://control.aps.amap.com/conf/r?type=3&mid=300&sver=140',
                    'http://control.aps.amap.com/conf/r?type=3&mid=300&sver=140'],
           'path': 'com/amap/location/a/c.java'}, {'urls': ['http://aps.testing.amap.com/dataPipeline/uploadData',
                                                            'https://cgicol.amap.com/dataPipeline/uploadData',
                                                            'http://cgicol.amap.com/dataPipeline/uploadData'],
                                                   'path': 'com/amap/location/uptunnel/core/b.java'},
       {'urls': ['javascript:(function(){function'], 'path': 'com/autonavi/nebulax/ui/titlebar/TinyBlurMenu.java'},
       {'urls': ['https://h5.m.taobao.com/'], 'path': 'com/autonavi/nebulax/plugin/TinyAppMTopPlugin.java'},
       {'urls': ['https://resource/'], 'path': 'com/autonavi/nebulax/extensions/H5OCRExtension.java'}, {
           'urls': ['http://sns.testing.amap.com/ws/feedback/report/', 'http://sns.amap.com/ws/feedback/report/',
                    'https://resource/(.*)', 'file:///'],
           'path': 'com/autonavi/nebulax/extensions/FeedbackBridgeExtension.java'},
       {'urls': ['https://wap.alipay.com'], 'path': 'com/autonavi/nebulax/extensions/PayCodeBridgeExtension.java'},
       {'urls': ['https://appx)切换', 'https://appx', 'https://appx)'],
        'path': 'com/autonavi/nebulax/debug/H5HomeListActivity.java'}, {
           'urls': ['https://cache.amap.com/h5/h5/publish/238/index.html',
                    'https://cache.amap.com/h5/h5/publish/241/index.html'],
           'path': 'com/autonavi/map/permission/PermissionPage.java'},
       {'urls': ['www.syncamap.com'], 'path': 'com/autonavi/cloudsync/NetWorkImpl.java'},
       {'urls': ['javascript:(function'], 'path': 'com/autonavi/widget/webview/inner/SafeWebView.java'},
       {'urls': ['javascript:(function'], 'path': 'com/autonavi/widget/webview/android/SafeWebView.java'},
       {'urls': ['http://wap.amap.com/callnative/?schema='],
        'path': 'com/autonavi/miniapp/plugin/share/MiniAppShareUtil.java'}, {
           'urls': ['http://wap.amap.com?type=', 'http://wap.amap.com', 'https://weibo.com/minimap',
                    'https://wap.amap.com/thanks/thanks.html'],
           'path': 'com/autonavi/mine/page/setting/sysabout/page/SysAboutPage.java'},
       {'urls': ['file:///'], 'path': 'com/autonavi/bundle/account/ajx/ModuleAccount.java'},
       {'urls': ['http://tpl.testing.amap.com'], 'path': 'com/autonavi/common/utils/Constant.java'},
       {'urls': ['http://autoapi.amap.com:80/ws/mps/vmap'], 'path': 'com/autonavi/link/proxy/net/Channel.java'}, {
           'urls': ['http://h5.edaijia.cn/amap/treaty.html', 'http://www.1jiajie.com/termsofservice.php',
                    'https://wap.amap.com/360/statement.html', 'http://wap.amap.com/user/plan.html'],
           'path': 'com/autonavi/minimap/widget/ConfirmDlg.java'},
       {'urls': ['file:///android_asset/connect_error.html', 'file:///android_asset/not_found_error.html'],
        'path': 'com/autonavi/minimap/landingpage/LandingPageHander.java'},
       {'urls': ['http://coverage.alibaba.net/api/coverage/v1/file/upload'],
        'path': 'com/autonavi/minimap/ajx3/upgrade/UploadCoverageTask.java'},
       {'urls': ['https://group.testing.amap.com/public/activity/life/viewpoint/exViewpointDetail.html'],
        'path': 'com/autonavi/minimap/life/order/viewpoint/page/ViewPointOrderDetailPage.java'}, {
           'urls': ['http://tpl.testing.amap.com/and/',
                    'https://h5.m.taobao.com/trip/hotel-react/order-detail/index.html'],
           'path': 'com/autonavi/minimap/life/order/hotel/page/OrderHotelDetailPage.java'},
       {'urls': ['https://ofo-amap.ofo.com/webapp/#/Repair/'],
        'path': 'com/autonavi/minimap/route/sharebike/page/ShareRidingMapPage.java'},
       {'urls': ['https://page.amap.com/ws/page/upload/'], 'path': 'com/autonavi/minimap/route/bundle/RouteVApp.java'},
       {'urls': ['http://f.amap.com/new/redirect?target='],
        'path': 'com/autonavi/minimap/route/coach/util/CoachPurchaseUtil.java'},
       {'urls': ['http://mps.amap.com', 'https://maps.testing.amap.com/', 'https://m5.amap.com/'],
        'path': 'com/autonavi/ae/gmap/AMapController.java'},
       {'urls': ['https://m5.amap.com/', 'https://maps.testing.amap.com/', 'https://mps.amap.com/'],
        'path': 'com/autonavi/ae/gmap/utils/GLMapServerUtil.java'}, {
           'urls': ['https://opencloud.wostore.cn/openapi/netauth/precheck/wp?',
                    'https://opencloud.wostore.cn/authz/oauth/token?timestamp='],
           'path': 'com/unicom/xiaowo/login/c/b.java'},
       {'urls': ['https://audid-api.taobao.com/v2.0/a/audid/req/'], 'path': 'com/ta/audid/upload/UtdidUploadTask.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#indent-output'],
        'path': 'com/ta/utdid2/core/persistent/XmlUtils.java'},
       {'urls': ['http://xmlpull.org/v1/doc/features.html#indent-output'],
        'path': 'com/ta/utdid2/core/persistent/FastXmlSerializer.java'}, {
           'urls': ['https://nbsdk-baichuan.alicdn.com/%s/component_config.htm',
                    'http://nbsdk-baichuan.taobao.com/%s/component_config.htm',
                    'http://100.69.205.47/%s/component_config.htm'],
           'path': 'com/alibaba/sdk/trade/container/license/AlibcContainerLicenseManager.java'},
       {'urls': ['https://arplatform.alicdn.com/x1app/sound_music/musicfile.wav'],
        'path': 'com/alibaba/coin/module/AINetSoundConfig.java'},
       {'urls': ['https://h-adashx.ut.taobao.com/upload'], 'path': 'com/alibaba/analytics/core/Constants.java'},
       {'urls': ['https://h-adashx.ut.taobao.com/upload'],
        'path': 'com/alibaba/analytics/core/sync/HttpsHostPortMgr.java'},
       {'urls': ['http://acs.m.taobao.com/gw/mtop.common.getTimestamp/*'],
        'path': 'com/alibaba/analytics/core/logbuilder/TimeStampAdjustMgr.java'}, {
           'urls': ['http://adash.m.taobao.com/rest/gc', 'http://adash.m.taobao.com/rest/er',
                    'http://adash.m.taobao.com/rest/tgc', 'http://adash.m.taobao.com/rest/ur'],
           'path': 'com/alibaba/analytics/core/device/Constants.java'},
       {'urls': ['https://m', 'https://act', 'https://.*', 'https://live', 'https://((a', 'https://(alipay'],
        'path': 'com/alibaba/ariver/permission/a/a.java'},
       {'urls': ['https://a.alipayobjects.com/bridgeapi/1.0/jsready.js', 'https://alipay.com/h5container/un_safe.html'],
        'path': 'com/alibaba/ariver/resource/api/content/ResourceProvider.java'}, {
           'urls': ['https://appx', 'https://appx-ng', 'https://appx/af-appx.min.js',
                    'https://appx/af-appx.worker.min.js'], 'path': 'com/alibaba/ariver/resource/runtime/a.java'},
       {'urls': ['https://appx'], 'path': 'com/alibaba/ariver/resource/runtime/ResourceLoadExtension.java'},
       {'urls': ['http://jsapi.inc.alipay.net:9999/ry'], 'path': 'com/alibaba/ariver/tools/connect/ConnectHelper.java'},
       {'urls': ['https://2015042700050887.hybrid.alipay-eco.com', 'https://2017021305648824.hybrid.alipay-eco.com',
                 'https://2015121700992100.hybrid.alipay-eco.com'],
        'path': 'com/alibaba/ariver/jsapi/security/OpenAuthExtension.java'},
       {'urls': ['file:///'], 'path': 'com/alibaba/ariver/kernel/common/utils/UrlUtils.java'}, {
           'urls': ['data:image/gif;base64,', 'data:image/x-icon;base64,', 'data:image/jpeg;base64,',
                    'data:image/png;base64,'], 'path': 'com/alibaba/ariver/kernel/common/utils/ImageUtil.java'},
       {'urls': ['https://alipay.kylinBridge'], 'path': 'com/alibaba/ariver/remotedebug/RDConstant.java'},
       {'urls': ['data:__workerjs});'], 'path': 'com/alibaba/ariver/remotedebug/worker/RemoteDebugWorker.java'},
       {'urls': ['https://alipay.kylinBridge'], 'path': 'com/alibaba/ariver/remotedebug/worker/JsApiHandler.java'},
       {'urls': ['https://resource/'], 'path': 'com/alibaba/ariver/commonability/file/a.java'},
       {'urls': ['https://resource/'], 'path': 'com/alibaba/ariver/commonability/file/e.java'},
       {'urls': ['https://resource/', 'https://usr/'],
        'path': 'com/alibaba/ariver/commonability/file/jsapi/FileBridgeExtension.java'},
       {'urls': ['https://appx/af-appx.worker.min.js'],
        'path': 'com/alibaba/ariver/engine/common/worker/BaseWorkerImpl.java'}, {
           'urls': ["javascript:window.AliBCBridge&&window.AliBCBridge.onFailure(%s,'%%s');",
                    "javascript:window.AliBCBridge&&window.AliBCBridge.onSuccess(%s,'%%s');"],
           'path': 'com/alibaba/baichuan/android/jsbridge/AlibcJsCallbackContext.java'},
       {'urls': ['https://h5.m.taobao.com/'], 'path': 'com/alibaba/baichuan/android/trade/AlibcContext.java'}, {
           'urls': ['https://detail.m.tmall.com/item.htm', 'https://h5.m.taobao.com/cm/snap/index.html',
                    'https://h5.m.taobao.com/awp/core/detail.htm', 'https://h5.m.taobao.com/trade/detail.html',
                    'https://h5.m.taobao.com/vip/portal.html', 'https://h5.m.taobao.com/mlapp/olist.html',
                    'https://bendi.m.taobao.com/coupon/q/eticket_detail.htm?isArchive=false',
                    'https://ff.win.taobao.com?des=promotions&cc=tae', 'https://shop.m.taobao.com/shop/shop_index.htm',
                    'https://h5.m.taobao.com/mlapp/cart.html', 'http://ff.win.taobao.com?des=promotions&cc=tae',
                    'http://ff.win.daily.taobao.net?des=promotions&cc=tae'],
           'path': 'com/alibaba/baichuan/android/trade/AlibcUrlCenter.java'},
       {'urls': ['http://muvp.alibaba-inc.com/online/UploadRecords.do'],
        'path': 'com/alibaba/baichuan/android/trade/adapter/ut/AlibcUserTracker.java'}, {
           'urls': ['http://nbsdk-baichuan.taobao.com/%s/%s/%s/meta.htm?plat=android',
                    'http://100.69.205.47/%s/%s/%s/meta.htm?plat=android',
                    'https://nbsdk-baichuan.alicdn.com/%s/%s/%s/meta.htm?plat=android'],
           'path': 'com/alibaba/baichuan/android/trade/constants/ConfigConstant.java'}, {
           'urls': ['http://100.69.205.47/authHint.htm?apiList=',
                    'http://pre.nbsdk-baichuan.taobao.com/authHint.htm?apiList=',
                    'https://nbsdk-baichuan.alicdn.com/authHint.htm?apiList='],
           'path': 'com/alibaba/baichuan/android/auth/c.java'},
       {'urls': ['https://login.sina.com.cn/visitor/signin'], 'path': 'com/weibo/ssosdk/WeiboSsoSdk.java'}, {
           'urls': ['https://gjapplog.ucweb.com/collect?uc_param_str=&chk=',
                    'https://applog.uc.cn/collect?uc_param_str=&chk='],
           'path': 'com/uc/webview/export/internal/uc/wa/a.java'},
       {'urls': ['https://long.open.weixin.qq.com/connect/l/qrconnect?f=json&uuid=%s'],
        'path': 'com/tencent/mm/opensdk/diffdev/a/f.java'}, {'urls': [
        'https://open.weixin.qq.com/connect/sdk/qrconnect?appid=%s&noncestr=%s&timestamp=%s&scope=%s&signature=%s'],
                                                             'path': 'com/tencent/mm/opensdk/diffdev/a/d.java'}, {
           'urls': ['https://openmobile.qq.com/user/user_login_statis', 'https://openmobile.qq.com/v3/user/get_info',
                    'http://appsupport.qq.com/cgi-bin/qzapps/mapp_addapp.cgi'],
           'path': 'com/tencent/connect/auth/AuthAgent.java'},
       {'urls': ['http://qzs.qq.com/open/mobile/login/qzsjump.html?'],
        'path': 'com/tencent/connect/auth/AuthDialog.java'},
       {'urls': ['https://openmobile.qq.com/'], 'path': 'com/tencent/connect/common/Constants.java'},
       {'urls': ['javascript:window.JsBridge&&JsBridge.callback('], 'path': 'com/tencent/open/a.java'},
       {'urls': ['http://qzs.qq.com/open/mobile/request/sdk_request.html?'],
        'path': 'com/tencent/open/SocialApiIml.java'},
       {'urls': ['http://c.isdspeed.qq.com/code.cgi'], 'path': 'com/tencent/open/b/d.java'},
       {'urls': ['http://cgi.qplus.com/report/report'], 'path': 'com/tencent/open/utils/Util.java'},
       {'urls': ['https://openmobile.qq.com/'], 'path': 'com/tencent/open/utils/HttpUtils.java'}, {
           'urls': ['http://fusion.qq.com/cgi-bin/qzapps/unified_jump?appid=%1$s&from=%2$s&isOpenAppID=1',
                    'http://fusion.qq.com/cgi-bin/qzapps/mapp_getappinfo.cgi',
                    'http://openmobile.qq.com/oauth2.0/m_authorize?', 'http://qzs.qq.com',
                    'http://qzs.qq.com/open/mobile/request/sdk_request.html?',
                    'http://qzs.qq.com/open/mobile/brag/sdk_brag.html?', 'https://openmobile.qq.com/',
                    'http://qzs.qq.com/open/mobile/invite/sdk_invite.html?',
                    'http://qzs.qq.com/open/mobile/reactive/sdk_reactive.html?', 'http://wspeed.qq.com/w.cgi',
                    'http://qzs.qq.com/open/mobile/sendstory/sdk_sendstory_v1.3.html?',
                    'http://qzs.qq.com/open/mobile/not_support.html?',
                    'http://qzs.qq.com/open/mobile/login/qzsjump.html?',
                    'http://qzs.qq.com/open/mobile/sdk_common/down_qq.htm?',
                    'http://openmobile.qq.com/oauth2.0/m_jump_by_version?', 'http://fusion.qq.com',
                    'http://fusion.qq.com/cgi-bin', 'http://fusion.qq.com/cgi-bin/prize_sharing/exchange_prize.cgi',
                    'http://fusion.qq.com/cgi-bin/prize_sharing/get_activity_state.cgi',
                    'http://fusion.qq.com/cgi-bin/prize_sharing/make_share_url.cgi',
                    'http://fusion.qq.com/cgi-bin/prize_sharing/query_unexchange_prize.cgi'],
           'path': 'com/tencent/open/utils/ServerSetting.java'},
       {'urls': ['http://cgi.connect.qq.com/qqconnectopen/openapi/policy_conf'],
        'path': 'com/tencent/open/utils/OpenConfig.java'},
       {'urls': ['https://id6.me/auth/preauth.do'], 'path': 'cn/com/chinatelecom/gateway/lib/a.java'},
       {'urls': ['http://schemas.android.com/apk/res/android'], 'path': 'pl/droidsonroids/gif/GifTextView.java'},
       {'urls': ['http://schemas.android.com/apk/res/android'], 'path': 'pl/droidsonroids/gif/GifTextureView.java'},
       {'urls': ['https://www.', 'http://www.'], 'path': 'org/altbeacon/beacon/utils/UrlBeaconUrlCompressor.java'},
       {'urls': ['https://)'], 'path': 'defpackage/ejt.java'},
       {'urls': ['https://cache.amap.com/tiny-app/shortcut/error_page/index.html?appId=%s&errorCode=%s'],
        'path': 'defpackage/dyw.java'},
       {'urls': ['https://store.hispace.hicloud.com/hwmarket/api/tlsApis'], 'path': 'defpackage/elp.java'},
       {'urls': ['file:///android_asset/'], 'path': 'defpackage/cfe.java'},
       {'urls': ['https://metrics.data.hicloud.com:6447'], 'path': 'defpackage/eia.java'},
       {'urls': ['http://%s:%d/%s'], 'path': 'defpackage/efe.java'},
       {'urls': ['http://mapdownload.autonavi.com/jefferyi/public/'], 'path': 'defpackage/pi.java'},
       {'urls': ['http://tpl.testing.amap.com/and/'], 'path': 'defpackage/aco.java'}, {
           'urls': ['https://mdn.alipayobjects.com/yaoyy_66666692/afts/file/A*2vSeTbuMu0gAAAAAAAAAAAAAAQAAAQ',
                    'https://mdn.alipayobjects.com/yaoyy_2019103068708979/afts/file/A*boKSSa359NsAAAAAAAAAAAAAAQAAAQ',
                    'https://mdn.alipayobjects.com/yaoyy_2021001106630355/afts/file/A*7XMiT6NJ40kAAAAAAAAAAAAAAQAAAQ'],
           'path': 'defpackage/dym.java'},
       {'urls': ['http://schemas.android.com/apk/res/android'], 'path': 'defpackage/esd.java'},
       {'urls': ['https://h5.m.taobao.com/trip/flight/myorder/list.html'], 'path': 'defpackage/atj.java'},
       {'urls': ['https://amap.com'], 'path': 'defpackage/cvv.java'},
       {'urls': ['https://render.alipay.com/p/s/upload-applog/index?account=%s'], 'path': 'defpackage/ayu.java'},
       {'urls': ['https://wap.amap.com/license/driving_1.html'], 'path': 'defpackage/buk.java'}, {
           'urls': ['https://github.com/danikula/AndroidVideoCache/issues/43.',
                    'https://github.com/danikula/AndroidVideoCache/issues.'], 'path': 'defpackage/efg.java'},
       {'urls': ['http://11.239.183.190:8090'], 'path': 'defpackage/eaz.java'},
       {'urls': ['https://hellobixi.taobao.com/demo/native-captcha-419'], 'path': 'defpackage/dbg.java'},
       {'urls': ['www.mapbar.com', 'http://www.weixin.com/?'], 'path': 'defpackage/dbt.java'},
       {'urls': ['http://f.amap.com/new/redirect?target='], 'path': 'defpackage/dvi.java'}, {
           'urls': ['https://wap.amap.com/license/driving.html', 'https://wap.amap.com/license/cleaning.html',
                    'https://wap.alipay.com'], 'path': 'defpackage/bux.java'},
       {'urls': ['file://external/'], 'path': 'defpackage/aid.java'},
       {'urls': ['file:///android_asset/'], 'path': 'defpackage/cbh.java'},
       {'urls': ['https://wap.amap.com/gxd/index.html', 'http://wb.amap.com/?'], 'path': 'defpackage/dbv.java'},
       {'urls': ['http://maps.aosdev.amap.com'], 'path': 'defpackage/cjp.java'},
       {'urls': ['http://tpl.testing.amap.com/and/'], 'path': 'defpackage/bdp.java'},
       {'urls': ['https://telematics.autonavi.com/sendtocar/?'], 'path': 'defpackage/cvk.java'},
       {'urls': ['https://m5.amap.com/', 'http://maps.testing.amap.com/'], 'path': 'defpackage/azr.java'}, {
           'urls': ['data:image/jpeg;base64', 'data:image/jpeg;base64,', 'data:image/png;base64',
                    'data:image/png;base64,'], 'path': 'defpackage/alb.java'},
       {'urls': ['file:///android_asset/'], 'path': 'defpackage/cbq.java'},
       {'urls': ['file:///data/data/com.autonavi.minimap/'], 'path': 'defpackage/anl.java'},
       {'urls': ["https://mobilegwpre.alipay.com/mgw.htm')", "https://mobilegw.alipay.com/mgw.htm')"],
        'path': 'defpackage/dxe.java'},
       {'urls': ['http://tpl.dev.myamap.com/andh/exData2car.html'], 'path': 'defpackage/cvt.java'},
       {'urls': ['https://github.com/danikula/AndroidVideoCache/issues/134.', 'http://%s:%d/%s'],
        'path': 'defpackage/efi.java'}, {'urls': ['www.syncamap.com'], 'path': 'defpackage/bgk.java'},
       {'urls': ['http://logs.amap.com/ws/log/upload/?in='], 'path': 'defpackage/bkn.java'}, {
           'urls': ['file:///android_asset/', 'file://external/', 'file://temporary/', 'file://documents/',
                    'file://aui_root/'], 'path': 'defpackage/nh.java'},
       {'urls': ['http://11.164.31.72:9922/busnavi?Type=2&ent=-1&Usr='], 'path': 'defpackage/dnh.java'},
       {'urls': ['file:///android_asset/'], 'path': 'defpackage/cbi.java'},
       {'urls': ['https://amap.com'], 'path': 'defpackage/cvj.java'}, {
           'urls': ['www.taobao.com18337258710将账户绑定到淘宝账户上', 'http://github.com/s12345678quare/leakcanary', 'http://www.amap.com',
                    'http://www.city8.com', 'http://www.leador.com.cn', 'http://www.tianya.tv', 'www.amap.com',
                    'www.openstreetmap.org/copyright', 'http://www.peacemap.com.cn/',
                    'http://www.elong.com/promotion/web/train/agreement.html', 'http://hf.weathercn.com/?user=gd',
                    'www.taobao.com', 'www.taobao.com將帳戶綁定到淘寶帳戶上'], 'path': 'Android String Resource'}]
print(len(dat))

class AnalysisUrlsEmails(object):
    def __init__(self,datas:list):
        self.datas = datas

    def extract_access_urls(self):  # 插入源码第一个函数，对code_an_dic['urls']进行解析，获取可以访问的urls
        """
        提取可访问的url
        :param urls: 需处理的url数据
        :return: 格式['urls':[],'path':'']，urls可访问
        """
        url_list = []
        for url in self.datas:
            need_url = []
            for url_ in url['urls']:
                if url_.lower().startswith('http'):
                    need_url.append(url_)
                elif url_.lower().startswith('www'):
                    url_ = 'http://' + url_
                    need_url.append(url_)
            if need_url:
                need_url = list(set(need_url))
                url_list.append({'urls': need_url, 'path': url['path']})
        return url_list

    @staticmethod
    def extract_phone_card_passport(data:str):
        """
        提取 手机号、身份证号、护照号
        :param data:需要利用re提取的数据
        :return:{'phones:[],'cards':[],'passports':[]}返回一个Dict类型
        """
        pattern_phone = re.compile(r'((1|0086|\+861)\d+)', re.UNICODE)
        phones = list(set([phone[0] for phone in re.findall(pattern_phone, data) if
                           (phone[0].startswith('1') and len(phone[0]) == 11) or (
                                   phone[0].startswith('0086') and len(phone[0]) == 15) or (
                                   phone[0].startswith('+86') and len(phone[0]) == 14
                           )]))
        pattern_card = re.compile(
            (r'(([1-6][1-9]|50)\d{4}(19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])|'
             r'(([1-6][1-9]|50)\d{4}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d+)'),
            re.UNICODE)
        cards = [card[0] if card[8] == '' else card[8] for card in re.findall(pattern_card, data)]
        pattern_passport = re.compile(
            (r'([EeKkGgDdSsPp]\d{8})|((([Ee][a-hjklmnp-zA-HJKLMNP-Z])|([DdSsPp][Ee])|([Kk][Jj])|([Mm][Aa]))\d{7})'),
            re.UNICODE)
        passports = [passport[1].upper() if passport[0] == '' else passport[0].upper() for passport in
                     pattern_passport.findall(data)]

        pattern_gps_lng = re.compile(
            (r'((\-|\+)?(((\d|[1-9]\d|1[0-7]\d|0{1,3})\.\d{0,7})|(\d|[1-9]\d|1[0-7]\d|0{1,3})|180\.0{0,7}|180))'),
            re.UNICODE
        )
        pattern_gps_lat = re.compile(
            (r'((\-|\+)?[0-8]?\d{1}\.\d{0,7}|90\.0{0,7}|[0-8]?\d{1}|90)'),
            re.UNICODE
        )
        lng = [lg[0] for lg in pattern_gps_lng.findall(data) if '.' in lg[0]]  # 经度 lng
        lat = [la[0] for la in pattern_gps_lat.findall(data) if '.' in la[0]]  # 经度 lat
        gps_lng_lat = [(ln,la) for ln in lng for la in lat]

        total = len(phones) + len(cards) + len(passports)
        if total != 0:
            return {'phones': phones, 'cards': cards, 'passports': passports,'gps_lng_lat':gps_lng_lat}

    def handle_urls_emails(self):
        """
        处理url与email数据
        :param datas: datas可以是url/email的列表
        :return:返回样式 [{},{}] --> {'urls'/'emails':[{'phones':[],'cards':[],'passports':[],'url/email':'xx'}],'path':'',}
        """
        # 判断参数是否存在urls与emails的key，如果是urls需要进行re处理，否则直接进行re处理邮箱
        if not len(self.datas):
            return []
        key = 'urls' if self.datas[0].get('urls') else 'emails'
        datas =self.extract_access_urls() if key == 'urls' else self.datas #对urls与emails做选择
        for data in datas:
            data_dict, need_datas = {}, []
            try:
                for tag in data[key]:  #处理data里面子列表
                    result = self.extract_phone_card_passport(tag) #进行正则处理
                    if result:
                        result[key.replace('s', '')] = tag  #添加具体哪个目标数据被解析出结果
                        need_datas.append(result) #将结果存入一个列表中
                data['results'] = need_datas #在源数据中插入结果列表的数据
                # results.append(data) #将每个path对应的urls解析结果进行保存
            except KeyError as e:
                print('遍历得到的data中缺少Key：%s' % e)
        return datas


# need_url  =AnalysisUrlsEmails(dat[0:3]).handle_urls_emails()
# print(need_url)



#handle_urls_emails 返回值


import time
# datas = extract_access_urls(dat)
# urls = sum([u['urls'] for u in datas], [])  #552
# urls = list(set(urls)) #425


# 异步解析response操作
import asyncio
import aiohttp
s_time = time.time()
class AnalysisResponse(object):
    def __init__(self,urls:list,datas:list,total=None,connect=None,sock_connect=15,sock_read=None):
        self.urls = urls
        self.datas = datas
        self.total = total
        self.connect = connect
        self.sock_connect = sock_connect
        self.sock_read = sock_read

    def __setitem__(self, k, v):
        self.k = v
    async def get(self,url):
        connector = aiohttp.TCPConnector(limit=10)
        timeout = aiohttp.ClientTimeout(total=self.total,connect=self.connect,
                                        sock_connect=self.sock_connect,
                                        sock_read=self.sock_read)
        async with aiohttp.ClientSession(timeout=timeout,connector=connector) as session:
            async with session.get(url) as rep:
                if rep.status == 200:
                    return {'url':url,'resp':await rep.text()}  # 返回响应内容
                    # return url, rep.headers #返回响应头信息
    async def request(self,url):

        print('await :%s'%url)
        try:
            result = await self.get(url)
            #得到响应内容
            return result

        except aiohttp.ClientConnectionError as e:
            #错误记录
            print('{0} <-- url: {1}'.format(e, url))
        except ValueError as e:
            print('{0} <-- url: {1}'.format(e, url))
        except UnicodeEncodeError as e:
            print('{0} <-- url: {1}'.format(e, url))
        # except asyncio.futures.TimeoutError as e:
        #     print('{0} <-- url: {1}'.format(e, url))
    def handle_resp(self,tasks):
        extract_url_response = []
        # [{'urls': ['https://api.weibo.cn/2/sdk/login13145652786',
        # 'http://e18727829api.weibo.cn/2/sdk/login'],
        #   'path': 'test1.java'},
        #   {'urls': ['https://service.weibo.com/share/mobilesdk_uppic.php89383898',
        #             'https://service.weibo.com/share/mobilesdk.php'],
        #   'path': 'test3.java'}]
        for task in tasks:
            if task.result():
                res = AnalysisUrlsEmails.extract_phone_card_passport(str(task.result()['resp'])) #re匹配响应内容(json/html)
                if res: #如果解析到数据,需要找出这个url的出处(来自哪个urls)
                    res['url'] = task.result()['url']
                    res['response'] = task.result()['resp']
                    for data in self.datas:  #遍历当前的全部数据源,
                        # data_dict, need_datas = {}, []
                        #如果response中解析到数据,,需要拼装
                        if res['url'] in data['urls']: #判断该url在哪个urls中出现,存在,在该data中的results的key中对应的字段添加值
                            # data['results'] = res
                            if data['results']: #如果第一次re没有匹配成功,那么该值为[] ,空列表,将测试resp解析的结果插入
                                pass


                        # else:data['results'] = []

                        extract_url_response.append(data)
        #得到的结果和第一步简单re匹配的结果是一样的,只是在results字段的结果集里面会多一个response字段
        # 接下来要进行合并

        #测试数据
        for data in self.datas:  # 遍历当前的全部数据源,
            data_dict, need_datas = {}, []
            # 如果response中解析到数据,,需要拼装

            i= 0
            print(len(tasks))
            for task in tasks:
                i = i + 1
                print('异步请求次数:%s'%(i))
                print('第一次正则的结果:%s' % data)
                if task.result():
                    print('进来了:%s'%(task.result()['url']))
                    # print(task.result()['resp'])  #添加测试数
                    r = '{msg:18337258719'
                    print('response:%s'%r)
                    # res = AnalysisUrlsEmails.extract_phone_card_passport(str(task.result()['resp']))  # re匹配响应内容(json/html)
                    res = AnalysisUrlsEmails.extract_phone_card_passport(r)  # re匹配响应内容(json/html)
                    print('解析结果:%s'%res)
                    if res:
                        res['url'] = task.result()['url']
                        # res['response'] = task.result()['resp']
                        res['response'] = r
                        if res['url'] in data['urls']:  # 判断该url在哪个urls中出现,存在,在该data中的results的key中对应的字段添加值
                            # data['results'] = res
                              # 如果第一次re没有匹配成功,那么该值为[] ,空列表,将测试resp解析的结果插入
                            if not data['results']:  #如果第一次的结果中results为空[] ,
                                print('第一次re时为空')
                                need_datas.append(res)
                                print(need_datas)
                            else: #不为空,需要判断此时url是否与结果中的某个url一样,如果一样需要将结果追加到已有的结果中
                                for r in data['results']:
                                    if r['url'] == res['url']:
                                        #存在,将resp的解析的结果,拼接在原有的results中
                                        r['phones'].extend(res['phones'])
                                        r['cards'].extend(res['cards'])
                                        r['passports'].extend(res['passports'])
                                        r['gps_lng_lat'].extend(res['gps_lng_lat'])
                                        r['response'] = res['response']  #将对应的response响应内容加上
                                    else:#不存在,在第一次的结果集中没有找到相等的url,则需要在结果集加上此时resp解析的结果
                                        need_datas.append(res)


            if need_datas:
                data['results'].extend(need_datas)
        print('最终结果:%s'%self.datas)
        return self.datas

    def run(self):

        tasks = [asyncio.ensure_future(self.request(url)) for url in self.urls[0:50]]
        # for task in tasks:if task.result()
        #     task.add_done_callback(self.callback)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        return self.handle_resp(tasks)  #返回response解析结果
        # return [extract_phone_card_passport(str(task.result()['rep'])) for task in tasks if task.result()]
# test = AnalysisResponse(urls).run()
# e_time = time.time()
# print(test)
# print(e_time-s_time)

def main(types:str,datas:list):  #注意：不能去重
    #开始匹配 %s : %types
    # print(datas)
    AUE = AnalysisUrlsEmails(datas=datas)
    first_result = AUE.handle_urls_emails()
    print('第一册')
    print(first_result)
    print('------------')
    if types == "urls":
        #开始匹配URL响应内容
        total_urls = list(set([l for u in first_result for l in u['urls']]))
        print(total_urls)
        #将access_urls 与 total_urls 传入,,access_urls用做比对
        resp_result = AnalysisResponse(urls=total_urls,datas=first_result).run()  #得到response对象
        #resp_result结果与第一步的一样,如果没用解析到




        #将解析的内容合并到第一步结果中
        # print(first_result)
        #
        # print(AR_result)

    elif types == "emails": return first_result
start_time = time.time()
main('urls',dat[0:5])
end_time = time.time()

print(end_time-start_time)