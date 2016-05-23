odoo.define('ch15_r04', function(require)
{
    var core = require('web.core'),
        data = require('web.data'),
        model = require('web.Model'),
        form_common = require('web.form_common');

    var FieldMany2OneButtons = form_common.AbstractField.extend({
        template: 'FieldMany2OneButtons',
        init: function()
        {
            var result = this._super.apply(this, arguments);
            this.on(
                'change:effective_readonly', this,
                this.effective_readonly_changed)
            return result;
        },
        events: {
            'click .btn': 'button_clicked',
        },
        willStart: function()
        {
            var deferred = new jQuery.Deferred(),
                self = this;
            self.user_list = {}
            new data.Query(new model(this.field.relation), ['display_name'])
            .filter(this.field.domain)
            .all()
            .then(function(records)
            {
                _.each(records, function(record)
                {
                    self.user_list[record.id] = record;
                    self.user_list[record.id].name = record.display_name;
                });
                deferred.resolve();
            });
            return jQuery.when(
                this._super.apply(this, arguments),
                deferred
            );
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
