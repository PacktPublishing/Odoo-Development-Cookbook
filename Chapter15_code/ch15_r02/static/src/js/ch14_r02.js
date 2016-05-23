odoo.define('ch15_r02', function(require)
{
    var core = require('web.core'),
        form_common = require('web.form_common');

    var FieldMany2OneButtons = form_common.AbstractField.extend({
        template: 'FieldMany2OneButtons',
        init: function()
        {
            var result = this._super.apply(this, arguments);
            this.user_list = {
                1: {
                    name: 'Administrator',
                },
                4: {
                    name: 'Demo user',
                },
            };
            this.on(
                'change:effective_readonly', this,
                this.effective_readonly_changed)
            return result;
        },
        events: {
            'click .btn': 'button_clicked',
        },
        set_value: function(_value)
        {
            this.$el.find('button').removeClass('btn-primary');
            this.$el.find(
                _.str.sprintf('button[data-id="%s"]',
                _.isArray(_value) ? _value[0] : _value)
            ).addClass('btn-primary');
            return this._super.apply(this, arguments);
        },
        button_clicked: function(e)
        {
            this.set_value(
                parseInt(jQuery(arguments[0].target).attr('data-id'))
            );
        },
        effective_readonly_changed()
        {
            this.$el.find('button').
                prop('disabled', this.get('effective_readonly'));
        },
    });

    core.form_widget_registry.add(
            'many2one_buttons', FieldMany2OneButtons);

    return {
        FieldMany2OneButtons: FieldMany2OneButtons,
    }
});
