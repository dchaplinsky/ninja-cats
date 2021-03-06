var fsBanner = function(container,options) {
    var self = this;

    var defaults = {
        'showName':true,
        'toUpdate':{},
        'whenEmpty':{},
        'trigger':'mouse',
        'hideParent':null,
        'onChanged':null,
        'parent': 'body'
    }

    this.options = $.extend({}, defaults, options);

    this.ilast = -1;

    this.setup = function() {
        var parentWidth = $(this.options.parent).width();
        this.container = $(container);
        this.items = this.container.find('div');

        this.part = parentWidth / this.items.length;
        this.mini = this.part/3;
        this.widmain = parentWidth - (this.mini*this.items.length-1);

        this.items.css({'height':this.container.height(),'width':this.widmain+this.mini});    

        if (!this.options.showName) this.items.find('.ttile').hide();

        this.items.each(function(i) {
            var $item = $(this);
            $item.css({'z-index':i});
            if (self.options.trigger == 'click') $item.on('click',function() { self.selectItem($item,i); });
            if (self.options.trigger == 'mouse') $item.on('mouseenter',function() {
                self.selectItem($item,i,true);
                self.items.removeClass('active');
                $item.addClass('active');
            });
            if (self.options.trigger == 'mouse') $item.on('mouseleave',function() {
                self.items.removeClass('active');
            });
        });

        if (self.options.trigger == 'mouse') {
            this.container.on('mouseleave',function() { self.resetcss(); });
        }

        this.resetcss();
        this.container.show();
    }

    this.resetcss = function() {
        this.items.each(function(i) {
            var $item = $(this);
            $item.stop().animate({'left':i*self.part});

            if (self.options.showName) {
                var $name = $item.find('.title');
                if ($name.hasClass('minimized')) $name.hide().removeClass('minimized').fadeIn('fast');
            }
        });
        this.ilast = null;
        this.updateHtml();
    };

    this.selectItem = function($expanded,iexpanded,forceClick) {
        this.$lastexpanded = this.$expanded;

        if (forceClick) this.ilast = null;
        if (iexpanded == this.ilast) {
            this.$expanded = null;
            this.resetcss();
        } else {
            this.$expanded = $expanded;
            this.items.each(function(i) {
                var $item = $(this);
                if (i <= iexpanded) {
                    $item.stop().animate({'left':i*self.mini});
                } else {
                    $item.stop().animate({'left':i*self.mini+self.widmain});
                }
                if (self.options.showName) {
                    var $name = $item.find('.title');
                    var method = (i == iexpanded) ? 'removeClass' : 'addClass';
                    if (method == 'addClass' && $name.hasClass('minimized')) method = '';
                    if (method) $name.hide()[method]('minimized').fadeIn('fast');
                }
            });
            this.ilast = iexpanded;
            this.updateHtml($expanded);
        }
        this.fireChanged();
    };

    this.updateHtml = function($expanded) {
        this.$expanded = $expanded;

        var $parent = $(self.options.hideParent);
        $.each(this.options.toUpdate,function(field,selector) {
            var $obj = $(selector);
            var showit = false;
            var value = '';
            if ($expanded) {
                $parent.show();
                value = $expanded.find('.'+field).html();
                showit = true;
            } else {
                if ($parent.length) {
                    showit = false;
                    $parent.hide();
                } else {
                    if (self.options.whenEmpty[field]) {
                        value = self.options.whenEmpty[field];
                        showit = true;
                    }
                }
            }
            $obj.hide();
            if (showit) $obj.html(value).fadeIn('fast');
        });
    };

    this.fireChanged = function() {
        if (this.options.onChanged) {
            this.options.onChanged(this.$expanded,this.$lastexpanded);
        }
    };

    this.setup();

    $(window).resize(function() {
        clearTimeout(window.resizedFinished);
        window.resizedFinished = setTimeout(function(){
            self.setup();
        }, 250);
    });
};

$.fn.fsBanner = function(options) {
    return new fsBanner(this,options);
};