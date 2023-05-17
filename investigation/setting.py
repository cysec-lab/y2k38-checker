_REPO = "/home/cysec/develop/y2k38-checker"
OUT_DIR             = _REPO + "/out"
CLANG_PATH          = _REPO + "/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang"
TOOL_RUN_DIRECTORY  = _REPO + "/build"
TOOL_PATH           = _REPO + "/build/bin/check-y2k38"

TARGET_ZIP_URLS = [
  {
    "name": "adafruit_Adafruit-Retrogame",
    "url": "https://github.com/adafruit/Adafruit-Retrogame/archive/refs/heads/master.zip"
  },
  {
    "name": "ailispaw_boot2docker-xhyve",
    "url": "https://github.com/ailispaw/boot2docker-xhyve/archive/refs/heads/master.zip"
  },
  {
    "name": "alexbw_Netflix-Prize",
    "url": "https://github.com/alexbw/Netflix-Prize/archive/refs/heads/master.zip"
  },
  {
    "name": "analang_como-lang-ng",
    "url": "https://github.com/analang/como-lang-ng/archive/refs/heads/master.zip"
  },
  {
    "name": "angel2d_angel2d",
    "url": "https://github.com/angel2d/angel2d/archive/refs/heads/master.zip"
  },
  # {
  #   "name": "AngelLiang_ESP8266-Demos",
  #   "url": "https://github.com/AngelLiang/ESP8266-Demos/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "aterrien_forp-PHP-profiler",
  #   "url": "https://github.com/aterrien/forp-PHP-profiler/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "bpaquet_ngx_http_enhanced_memcached_module",
  #   "url": "https://github.com/bpaquet/ngx_http_enhanced_memcached_module/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "bwhite_hadoopy",
  #   "url": "https://github.com/bwhite/hadoopy/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "Byzantium_Byzantium",
  #   "url": "https://github.com/Byzantium/Byzantium/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "carl-wang-cn_demo",
  #   "url": "https://github.com/carl-wang-cn/demo/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "cetic_6lbr",
  #   "url": "https://github.com/cetic/6lbr/archive/refs/heads/develop.zip"
  # },
  # {
  #   "name": "cjlano_freertos",
  #   "url": "https://github.com/cjlano/freertos/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "clarkgrubb_data-tools",
  #   "url": "https://github.com/clarkgrubb/data-tools/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "Cloudef_orbment",
  #   "url": "https://github.com/Cloudef/orbment/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "cnlohr_espthernet",
  #   "url": "https://github.com/cnlohr/espthernet/archive/refs/heads/gh-pages.zip"
  # },
  # {
  #   "name": "cnlohr_ws2812esp8266",
  #   "url": "https://github.com/cnlohr/ws2812esp8266/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "cofyc_dnscrypt-wrapper",
  #   "url": "https://github.com/cofyc/dnscrypt-wrapper/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "cyburgee_loopFindr",
  #   "url": "https://github.com/cyburgee/loopFindr/archive/refs/heads/threaded-processing.zip"
  # },
  # {
  #   "name": "Denton-L_based-connect",
  #   "url": "https://github.com/Denton-L/based-connect/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "dimonomid_tneo",
  #   "url": "https://github.com/dimonomid/tneo/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "dismantl_linux-injector",
  #   "url": "https://github.com/dismantl/linux-injector/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "dndx_shadowsocks-libuv",
  #   "url": "https://github.com/dndx/shadowsocks-libuv/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "doggycoder_AudioVideo",
  #   "url": "https://github.com/doggycoder/AudioVideo/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "dreamsxin_cphalcon7",
  #   "url": "https://github.com/dreamsxin/cphalcon7/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "esl_erlang_ale",
  #   "url": "https://github.com/esl/erlang_ale/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "etolabo_kumofs",
  #   "url": "https://github.com/etolabo/kumofs/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "eviltrout_tis-100",
  #   "url": "https://github.com/eviltrout/tis-100/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "face_MongooseDaemon",
  #   "url": "https://github.com/face/MongooseDaemon/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "facebookarchive_atosl",
  #   "url": "https://github.com/facebookarchive/atosl/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "facebookarchive_liblogfaf",
  #   "url": "https://github.com/facebookarchive/liblogfaf/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "fanchy_fflib",
  #   "url": "https://github.com/fanchy/fflib/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "fhunleth_elixir_ale",
  #   "url": "https://github.com/fhunleth/elixir_ale/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "fjolnir_xnomad",
  #   "url": "https://github.com/fjolnir/xnomad/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "FuruyamaTakeshi_DLNA",
  #   "url": "https://github.com/FuruyamaTakeshi/DLNA/archive/refs/heads/develop.zip"
  # },
  # {
  #   "name": "FuzzySecurity_Unix-PrivEsc",
  #   "url": "https://github.com/FuzzySecurity/Unix-PrivEsc/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "gabriel_yajl-objc",
  #   "url": "https://github.com/gabriel/yajl-objc/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "gameoverhack_ofxOpenNI",
  #   "url": "https://github.com/gameoverhack/ofxOpenNI/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "gianlucabertani_Objective-Zip",
  #   "url": "https://github.com/gianlucabertani/Objective-Zip/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "git-mirror_nginx",
  #   "url": "https://github.com/git-mirror/nginx/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "gregkh_kdbus",
  #   "url": "https://github.com/gregkh/kdbus/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "guokr_gkseg",
  #   "url": "https://github.com/guokr/gkseg/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "H2CO3_Sparkling",
  #   "url": "https://github.com/H2CO3/Sparkling/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "HaJaeKyung_KittyExtension",
  #   "url": "https://github.com/HaJaeKyung/KittyExtension/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "heardrwt_RevealLoader",
  #   "url": "https://github.com/heardrwt/RevealLoader/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "hpricot_hpricot",
  #   "url": "https://github.com/hpricot/hpricot/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "HunterHillegas_iOS-BetaBuilder",
  #   "url": "https://github.com/HunterHillegas/iOS-BetaBuilder/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "HuoLanguage_huo",
  #   "url": "https://github.com/HuoLanguage/huo/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "iceonsun_rsock",
  #   "url": "https://github.com/iceonsun/rsock/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "ilg-archived_qemu",
  #   "url": "https://github.com/ilg-archived/qemu/archive/refs/heads/gnuarmeclipse-dev.zip"
  # },
  # {
  #   "name": "imatix_gsl",
  #   "url": "https://github.com/imatix/gsl/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "immobiliare_sfs",
  #   "url": "https://github.com/immobiliare/sfs/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "iondbproject_iondb",
  #   "url": "https://github.com/iondbproject/iondb/archive/refs/heads/development.zip"
  # },
  # {
  #   "name": "JaciBrunning_Pathfinder",
  #   "url": "https://github.com/JaciBrunning/Pathfinder/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "JaneaSystems_nodejs-mobile-react-native",
  #   "url": "https://github.com/JaneaSystems/nodejs-mobile-react-native/archive/refs/heads/unstable.zip"
  # },
  # {
  #   "name": "JazzCore_ctrlp-cmatcher",
  #   "url": "https://github.com/JazzCore/ctrlp-cmatcher/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "jduck_asus-cmd",
  #   "url": "https://github.com/jduck/asus-cmd/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "Jekub_Wapiti",
  #   "url": "https://github.com/Jekub/Wapiti/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "jintiao_some-mmorpg",
  #   "url": "https://github.com/jintiao/some-mmorpg/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "jkramer_shell-fm",
  #   "url": "https://github.com/jkramer/shell-fm/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "jwgrenning_tddec-code",
  #   "url": "https://github.com/jwgrenning/tddec-code/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "jwilberding_bcp",
  #   "url": "https://github.com/jwilberding/bcp/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "jyr_MNPP",
  #   "url": "https://github.com/jyr/MNPP/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "karthick18_inception",
  #   "url": "https://github.com/karthick18/inception/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "kazeburo_rhebok",
  #   "url": "https://github.com/kazeburo/rhebok/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "kennyyu_workshop",
  #   "url": "https://github.com/kennyyu/workshop/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "kholia_dedrop",
  #   "url": "https://github.com/kholia/dedrop/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "krakjoe_phpdbg",
  #   "url": "https://github.com/krakjoe/phpdbg/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "Kreijstal_Random-C-stuff",
  #   "url": "https://github.com/Kreijstal/Random-C-stuff/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "lilac_Android-ImageMagick",
  #   "url": "https://github.com/lilac/Android-ImageMagick/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "limccn_Cocoa-Charts",
  #   "url": "https://github.com/limccn/Cocoa-Charts/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "linklayer_cantact-fw",
  #   "url": "https://github.com/linklayer/cantact-fw/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "Lokaltog_candybar",
  #   "url": "https://github.com/Lokaltog/candybar/archive/refs/heads/develop.zip"
  # },
  # {
  #   "name": "lowlevel86_3D-Game-Programming",
  #   "url": "https://github.com/lowlevel86/3D-Game-Programming/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "lpan_viw",
  #   "url": "https://github.com/lpan/viw/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "lsds_spectre-attack-sgx",
  #   "url": "https://github.com/lsds/spectre-attack-sgx/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "ltebean_novel-design",
  #   "url": "https://github.com/ltebean/novel-design/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "lukeweber_webrtc-jingle-client",
  #   "url": "https://github.com/lukeweber/webrtc-jingle-client/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "lzyickobe_UnInstallDemo",
  #   "url": "https://github.com/lzyickobe/UnInstallDemo/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "madlib_archived_madlib",
  #   "url": "https://github.com/madlib/archived_madlib/archive/refs/heads/placeholder.zip"
  # },
  # {
  #   "name": "matricks_teeworlds",
  #   "url": "https://github.com/matricks/teeworlds/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "mattt_WebPImageSerialization",
  #   "url": "https://github.com/mattt/WebPImageSerialization/archive/refs/heads/main.zip"
  # },
  # {
  #   "name": "menudoproblema_libemqtt",
  #   "url": "https://github.com/menudoproblema/libemqtt/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "microsoft_pg_paxos",
  #   "url": "https://github.com/microsoft/pg_paxos/archive/refs/heads/main.zip"
  # },
  # {
  #   "name": "mkoppanen_php-zbarcode",
  #   "url": "https://github.com/mkoppanen/php-zbarcode/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "mkusner_wmd",
  #   "url": "https://github.com/mkusner/wmd/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "Mon-Ouie_ray",
  #   "url": "https://github.com/Mon-Ouie/ray/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "MonetDB_MonetDB-old",
  #   "url": "https://github.com/MonetDB/MonetDB-old/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "monome_libmonome",
  #   "url": "https://github.com/monome/libmonome/archive/refs/heads/main.zip"
  # },
  # {
  #   "name": "moqod_ios-qr-code-encoder",
  #   "url": "https://github.com/moqod/ios-qr-code-encoder/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "mozilla-services_ios-sync-client",
  #   "url": "https://github.com/mozilla-services/ios-sync-client/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "mrcao2011_ProgressView",
  #   "url": "https://github.com/mrcao2011/ProgressView/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "mstorsjo_vlc-android",
  #   "url": "https://github.com/mstorsjo/vlc-android/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "myafer_OpenSSLApplication",
  #   "url": "https://github.com/myafer/OpenSSLApplication/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "NagiosEnterprises_nrpe",
  #   "url": "https://github.com/NagiosEnterprises/nrpe/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "norbusan_sony-laptop-zseries",
  #   "url": "https://github.com/norbusan/sony-laptop-zseries/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "OculusRiftInAction_OculusRiftInAction",
  #   "url": "https://github.com/OculusRiftInAction/OculusRiftInAction/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "ONsec-Lab_scripts",
  #   "url": "https://github.com/ONsec-Lab/scripts/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "osresearch_LEDscape",
  #   "url": "https://github.com/osresearch/LEDscape/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "paixaop_node-sodium",
  #   "url": "https://github.com/paixaop/node-sodium/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "pakt_ropc",
  #   "url": "https://github.com/pakt/ropc/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "PebbleSeizureDetect_PebbleSeizureDetect",
  #   "url": "https://github.com/PebbleSeizureDetect/PebbleSeizureDetect/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "peter-leonov_ngx_http_js_module",
  #   "url": "https://github.com/peter-leonov/ngx_http_js_module/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "pez2001_razer_chroma_drivers",
  #   "url": "https://github.com/pez2001/razer_chroma_drivers/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "python_typed_ast",
  #   "url": "https://github.com/python/typed_ast/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "qiye_redis-storage",
  #   "url": "https://github.com/qiye/redis-storage/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "rainyx_rxmemscan",
  #   "url": "https://github.com/rainyx/rxmemscan/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "redbo_cloudfuse",
  #   "url": "https://github.com/redbo/cloudfuse/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "RedisLabsModules_redisml",
  #   "url": "https://github.com/RedisLabsModules/redisml/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "Reisyukaku_ReiNand",
  #   "url": "https://github.com/Reisyukaku/ReiNand/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "rpeshkov_IntelWifi",
  #   "url": "https://github.com/rpeshkov/IntelWifi/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "slavavdovichenko_MediaLibDemos3x",
  #   "url": "https://github.com/slavavdovichenko/MediaLibDemos3x/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "solettaproject_soletta",
  #   "url": "https://github.com/solettaproject/soletta/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "sonsongithub_CoreAR",
  #   "url": "https://github.com/sonsongithub/CoreAR/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "souliss_souliss",
  #   "url": "https://github.com/souliss/souliss/archive/refs/heads/friariello.zip"
  # },
  # {
  #   "name": "soveran_map",
  #   "url": "https://github.com/soveran/map/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "SS-archive_salt-states",
  #   "url": "https://github.com/SS-archive/salt-states/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "stelgenhof_AiLight",
  #   "url": "https://github.com/stelgenhof/AiLight/archive/refs/heads/develop.zip"
  # },
  # {
  #   "name": "swetland_dcpu16",
  #   "url": "https://github.com/swetland/dcpu16/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "tailhook_zerogw",
  #   "url": "https://github.com/tailhook/zerogw/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "tg123_chrome-hostadmin",
  #   "url": "https://github.com/tg123/chrome-hostadmin/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "tharina_BlackHoodie-2018-Workshop",
  #   "url": "https://github.com/tharina/BlackHoodie-2018-Workshop/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "therealdreg_anticuckoo",
  #   "url": "https://github.com/therealdreg/anticuckoo/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "thestinger_playpen",
  #   "url": "https://github.com/thestinger/playpen/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "tmm1_rblineprof",
  #   "url": "https://github.com/tmm1/rblineprof/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "torch_DEPRECEATED-torch7-distro",
  #   "url": "https://github.com/torch/DEPRECEATED-torch7-distro/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "unbit_spockfs",
  #   "url": "https://github.com/unbit/spockfs/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "UWNetworksLab_arrakis",
  #   "url": "https://github.com/UWNetworksLab/arrakis/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "vipshop_vire",
  #   "url": "https://github.com/vipshop/vire/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "watmough_jwHash",
  #   "url": "https://github.com/watmough/jwHash/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "wolfgangfengel_GPUZen",
  #   "url": "https://github.com/wolfgangfengel/GPUZen/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "yhirano_Mp3VoiceRecorderSampleForAndroid",
  #   "url": "https://github.com/yhirano/Mp3VoiceRecorderSampleForAndroid/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "youzan_zan",
  #   "url": "https://github.com/youzan/zan/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "yoyofx_NetCore_YOYOFx",
  #   "url": "https://github.com/yoyofx/NetCore_YOYOFx/archive/refs/heads/Dev.zip"
  # },
  # {
  #   "name": "yunnian_php-nsq",
  #   "url": "https://github.com/yunnian/php-nsq/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "zebrafishlabs_nginx-statsd",
  #   "url": "https://github.com/zebrafishlabs/nginx-statsd/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "zeromq_zproto",
  #   "url": "https://github.com/zeromq/zproto/archive/refs/heads/master.zip"
  # },
  # {
  #   "name": "zhoubolei_cnnvisualizer",
  #   "url": "https://github.com/zhoubolei/cnnvisualizer/archive/refs/heads/master.zip"
  # }
]
